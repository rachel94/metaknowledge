Hi! If you're reading this it means you've been tasked with completing the conversion of the mk docs to Read the Docs (rtd). This should help you understand what I've done, what's left to be done, and how I think it could be done.

## Overview
If you have any questions, I'm happy to chat about this. You can message me on Mattermost or email me at <a href="mailto:rewood34@gmail.com">rewood34@gmail.com</a> (an email will likely guarantee a quicker response if I'm not online on Mattermost at the time). I think it would be useful to meet up or have a video chat about this, you can let me know if you agree and I'm happy to set something up!

The existing docs for metaknowledge are <a href="http://networkslab.org/metaknowledge/documentation/metaknowledgeFull">here</a>.

You can find everything relating to documentation (scripts, templates, the docs themselves) in metaknowledge/metaknowledge/docs.

I'm going to first explain how this all works generally, and then I'll explain what still needs to be done. What still needs to be done is titled "What's left to do", and is farther down this doc.

## Setting up the docs for Read the Docs
I started by doing <a href="https://docs.readthedocs.io/en/latest/getting_started.html">this tutorial</a> from Read the Docs. I opted to use reStructuredText (rst) simply because the tutorial for it seemed easier. If you'd rather use Markdown and think it won't be too difficult to change (or to use both together) feel free to do so (though everything I've done so far has been in rst). Following the tutorial and using `sphinx quickstart`, the following were created:
* `/build` (this is where the generated html pages go)
* `/build/doctrees` (this was generated automatically when I generated the html pages, and I believe it keeps track of how the various html pages are linked together)
* `/static` (So far this is empty. I assume this is where you'd put custom CSS or JS if you needed it, though rtd has built in styling that has mostly been sufficient so far. You might find a use for some additional styles though, so I think they'd go here.)
* `/templates` (this is also empty, I'm not sure what you'd put here)
* `conf.py` (this is an important file, I believe I changed all the necessary values within it. you'll learn about it in the above tutorial if you do that)
* `make.bat` (this is needed to generate your html files)
* `Makefile` (this is needed to generate your html files)

I then added the following:
* `index.rst` (this is the main page of the docs on read the docs. the *toctree* is super important within it, and is explained in the above tutorial. Otherwise, you can put whatever content you want; so I put the intro text for metaknowledge from the old documentation)
* all the other files ending in .rst (these are the other pages at the top level of our read the docs file structure)
* all other subdirectories (these contain more pages that make up our docs, but that are nested)
* `regex.md` (contains a list of some useful regular expressions I've been using to find and replace parts of the docstrings. You will likely end up creating more of these, but they speed things up a lot – more on how the existing docstrings contribute to this later)

## Generating HTML pages for Read the Docs
Essentially what's happening is we're creating RST pages, and then using Sphinx to convert this into HTML that works with the styling of RTD. If there are any errors they will show up in the command line – I've found that there can often be little errors that are basically telling you that something with your syntax is wrong which will break the way it should work in RTD.

Some of the pages, such as the index page, were pretty easy to create because I just copied it from the existing docs, and made it into RST myself. However, we also want to use the existing docstrings that are found throughout the metaknowledge package, and have those be automatically converted to RST. This has been done for the Modules and Exceptions, and still needs to be done for Functions & Methods, and Classes. The RST docs are created by running getClasses.py, getModules.py, and getExs.py (we still need to write this for the Functions & Methods, and finish getClasses – more on this later). So the idea is that whenever you update the code in mk, and the docstrings, you would run each of these, and then run this command to convert this into HTML: `cd [wherever you stored this repo]/metaknowledge/metaknowledge/docs`
`make html` (more on this below). This would allow the docs on RTD to be updated to match the changes to mk by typing just a few lines.

### restructuredText (RST)
If you continue to use RST like I've been, you can learn the syntax <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html">here</a>. Some things are kind of annoying in RST, such as making a hyperlink italicized, because it doesn't allow for nested styles (which was super annoying). However, there are weird workarounds to this, where you sort of put in a variable, and then replace the variable later. Take a look at `install.rst` for some examples of this. Or, if you're using markdown, use that syntax instead.

### Converting from RST to HTML
When you've generated some pages in RST and are ready to convert them to HTML, simply do the following on the command line:
`cd [wherever you stored this repo]/metaknowledge/metaknowledge/docs`
`make html`
This generates the .html files from the .rst files, and puts them in `/build`. You can then view them in a browser by just opening the .html pages. If there's an error in the rst files (usually it's something to do with the links in your toctrees, or other syntax errors), read the error messages in Terminal/cmd bc they're usually pretty helpful.

## Getting the files live on Read the Docs
I've made aan account with RTD where I'd been hosting the docs. I mostly did this for learning purposes, but ultimately this will need to be hosted on an account that John should probably set up, or use like a shared Netlab account or something. I'll leave mine up for a bit in case I need to look back at it to remember how I did it, but then I'll take mine offline. You can still test what the files will look like on RTD just by opening the .html files in a browser, so you don't *need* to make your own RTD account to do this. If you're interested, <a href="https://mk-july6.readthedocs.io/en/latest/">here is my hosted version</a>. (Don't be alarmed if I've taken it down by the time you read this).

### Steps to get the files live on Read the Docs
For whoever will be putting the docs on RTD, essentially you do the following (there are more thorough tutorials online):
1. Make a <a href="https://readthedocs.org/">Read the Docs</a> account
2. Go to the dropdown beside your username in the top right corner and click **My Projects**
3. Click **Import a Project**
4. Click **Import Manually** (unless what you're looking for shows up automatically if you've linked your GitHub account to RTD, in which case click on it)
5. Provide the URL to your git repo where the docs are (I think your repo needs to be public to work with this)
6. Now you also have to add a webhook in your repo. This allows any new pushes to your repo to automatically push to RTD too. If you're using GitHub, go to your repo's settings > **WebHooks** > **Add webhook**. For 'Payload URL', you put in the URL that you can find on RTD under **Projects** > **your project (mk)** > **Admin** > **Integrations**. There should be a link there that will say it can be used for incoming webhooks.
7. Then if it hasn't built already, (in RTD) go to **Projects** / **your project** / **Overview**, and click **Build**.
8. You can view the docs by clicking **View Docs**
9. When you make changes to your docs, make sure you run all the necessary scripts to convert the docstrings to RST (see below), then run `make html` to remake the html pages, then push to git. This should automatically make the changes on RTD.

## Understanding the scripts I wrote
We want the docs to be automatically generated from the docstrings that already exist with each module, class, function, methods, and the exceptions.

So I've written `getModules` which gets all these docstrings from the modules' docstrings and writes it to the proper RST files (in `metaknowledge/docs/documentation/modules/` – then there's one for each of the six modules there: WOS, contour, medline, scopus, proquest, journalAbbreviations). I also have `getExs` that gets the docstrings from the Exceptions (in `mkExceptions.py`) and puts all of that in one RST file (in `metaknowledge/docs/documentation/exceptions/index.rst`). I've also written the beginnings of `getClasses`, which will get all the docstrings from each location where any of the classes are (see list below for where you can find these). This will then go into each of the RST files in `metaknowledge/docs/documentation/classes/`. These scripts can all be found in `metaknowledge/docs/`

There's more comments about the scripts in the py files themselves. `getExs` is a fair bit simpler so it might be a good place to start. `getModules` is the first one I wrote and could use some simplifying as it has some unecessary repetition. `getClasses` is not yet done.

As a side note, Reid had already written a script <a href="https://github.com/rachel94/metaknowledge/blob/master/metaknowledge/bin/metaknowledgeDocsGen.py">`metaknowledge/metaknowledge/bin/metaknowledgeDocsGen.py`</a> that converts all the docstrings to markdown that was used to create the original custom mk docs. However, I ended up writing my own scripts, as I described above.

### Organizing the docs
Here is how I intended the docs to be organized, and how I think is a reasonable way to continue organizing them on RTD. Each list element represents a separate RST page, and therefore a separate HTML page.

* Intro (index file – done)
* Installation – done
* Documentation
    * Overview – done except for some faulty links, which will need to be fixed
    * Examples – done
    * Functions &amp; Methods (\*needed\*)
    * Exceptions – done
        * there are just some faulty links that need to be fixed
        * In the existing docs, there are no descriptions provided with the exceptions, but some of the exceptions in `mkExceptions` have docstrings listed. I've included these, but they're easy enough to remove them if you'd like

    * Classes. Each class and their docstrings can be found in the listed py file:
        * WOSRecord class: `WOS/recordWOS.py`
    		* citation class: `citation.py`
    		* Grant Collection class: `grantCollection.py`
    		* Grant class: `grants/baseGrant.py`
    		* NSERC Grant class: `grants/NSERCGrant.py`
    		* NSFGrant class: `grants/NSFGrant.py`
    		* medline record class: `medline/recordMedline.py`
    		* collection class: `mkCollection.py`
    		* collection with IDs class: `mkCollection.py`
    		* extended record class: `mkRecord.py`
    		* record class: `mkRecord.py`
    		* proquest record class: `proquest/recordProQuest.py`
    		* record collection class: `recordCollection.py`
        * scopus record class: `scopus/recordScopus.py`

    * Modules
        * Contour – done
        * Journal Abbreviations – see below for quick fix needed
        * Medline – done
        * Proquest – see below for quick fix needed
        * Scopus – done
        * WOS – see below for quick fix needed

* Examples (from jupyter notebooks – see below)
* Command Line Tool (done, but think we're removing this – see below)

### The details of the scripts
Basically `writeModFiles` in `getModules.py` uses the `ast` Python package to identify what parts of the files in those modules are docstrings, functions, parameters, and defaults. It reads the `__init__.py` file to find the overall docstrings (like an intro to the module). Then it opens any file that's not `__init__.py` and uses `ast` to find the functions (but not the classes). These get added to the new RST file first as part of a table of contents. I chose to do this to follow the way the existing docs are, bc I thought it's useful for the pages that will have more functions. However, I'm running into trouble making links to different parts of the page with IDs in RST (see below), so right now the table of contents is just visual and not functional and therefore fairly counter productive. Anyway, then below that, the function and its parameters and defaults are listed (also found using the `ast` package), then the docstrings for that individual function, formatted to match the way the existing docs did it.

There's more explanation of the scripts in comments within the py files.

In "What's left to do" below, I explain what still needs to be done. Feel free to use pieces of Reid's code as well for that. While I ended up rewriting a lot, his could still be used with some modifications.

### Converting the docstrings to work with RST
In order to make the docstrings convert properly to RST, I needed to make changes to the docstrings in each of the `.py` files. I did most of this using regular expressions, which you can find in <a href="https://github.com/rachel94/metaknowledge/blob/master/metaknowledge/docs/regex.md">regex.md</a>. Once you get going with this it doesn't take too long. Essentially what you're doing is changing them from markdown to RST, so that when our scripts read it in, it's already in RST. <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html">This document about the RST syntax</a> will prove useful for this too, but you don't have to change *everything* so I'm hoping what remains won't be too time consuming to do.

### Running the scripts!
When you want to run the scripts to generate the RST files from any updated docstrings,  `cd` into `metaknowledge/docs`, and then run each script. Do this anytime you update your docstrings or change functions. Then type `make html`. this converts the RST to html files for RTD. If you're ready to make this live, then push to git to make it accessible on RTD.

## What's left to do

### Making sure all the proper functions are in each module's page
I don't *quite* have all the functions in each of the 6 modules' docs, so they aren't quite done yet.
`countour`, `scopus`, and `medline` are done. They are in a different order than those in the existing docs, but I don't think this matters.
`proquest` is done too but I'm not sure if it also needs the other functions from `proquest/tagProcessing/tagFunctions.py`? You might need to ask John about this.
`journalAbbreviations` has all the functions that are in the existing docs, but it also has some others. I don't know if those are supposed to be there or not? In the original, there is only `addToDB` and `getj9Dict`. Ask John if the others need to be there. If they do, leave it. If they don't, modify the code to restrict it to only those functions with that name when `mod == 'journalAbbreviations'`.
`WOS` is missing the following: `getMonth`. Ask John if this is still needed? Try to find it in the WOS files somewhere, I'm not sure why it's not been included, unless maybe it doesn't exist anymore?

### Generating the docs for functions, classes, methods
I started a function that gets the docstrings for classes, `getClasses`. It currently only works for `citation.py`, but it will need to be extended to generate docs for all of the classes. They should all be pretty similar so this should just involve some generalizing. In the list above you can see where each of these classes are located in the file structure. With the current state of `getClasses`, it's creating one error in Sphinx (you can see this in the command line when you run `getClasses`).

For functions and methods, it should be similar, but you need to find where these functions and methods are in the metaknowledge package, and then open those files, read the docstrings, and generate RST files in the appropriate directory. It should still be pretty similar to `getModules`, it will just involve finding the functions first. You can see what all these functions and methods are <a href="http://networkslab.org/metaknowledge/documentation/metaknowledgeFull#fulllist">here, in the existing docs</a>.

Remember that you will have to modify the docstrings in all of these files too, so that they conform to RST.

### One script that runs all the others
This should be fairly trivial to implement, but I think it might be useful to have one script that just calls the other four (`getExs`, `getModules`, `getClasses`, `getFunctions`). But I guess an argument against that is if there's situations where you'd only want to be running one of those at a time. I'll leave this up to you.

### Hyperlinks within each documentation page (and adding IDs)
This is something I've found pretty difficult (implementing hyperlinks and IDs in RST). There are many hyperlinks within the current mk docs, to jump to different sections of the current page. Since we've separated our docs up into different pages to be used on RTD, this now means hyperlinking both within the same page, and throughout the pages. I do think this is still important to do, as it improves usability.

I have some of the hyperlinks working now, and a good place to see this is on the proQuest page.

#### Hyperlinks to different pages
The hyperlinks within the docs for a given function had to be implemented in the docstrings themselves. For instance, in `proquest/proQuestHandlers.py`, you can find the following text: "The returned `ProQuestRecords <../classes/proquestrecord.html>`__ contains the data from the second section," (if this isn't displaying right here, open this in a text editor). This hyperlink goes to another page in the RTD docs. So in general you should be able to implement hyperlinks like that to link to other pages in the docs. Finding which need to be hyperlinked may take some time, but I kind of just followed how the existing docs are.

#### Hyperlinks within the same page (or anything relying on IDs)
I've been having trouble adding IDs to the HTML elements, since it's all generated via RST, but I believe RST generates IDs automatically for the headings. Ideally, the tables of contents at the top of each page (not the toctree but like the list of functions on a given page), will actually be clickable and jump to the correct part of the page. This would need to be added right in the script, since that's where the table of contents entries are added (by this I mean like how in the proquest page it says "The proquest module provides the following functions" and then provides a list of the functions). If RST doesn't create IDs for headings automatically, then the IDs would also need to be added in the script, since that's where we create the headings.

There are also hyperlinks in the existing docs that should link to functions, etc., that will be on the same page even in our docs, so ideally we would be able to use the IDs that exist on the heading of the target destination, and add a link to jump there. Any hyperlinks within the docstrings would need to be added by the method described above, but would need to link to an ID on the same page rather than to a different page.

For example, on the proquest page, **isProQuestFile** should have an ID associated with it. There's a mention of **isProQuestFile** later on in the page, that should be hyperlinked and jump back up to that heading, but it's currently not working. So that's an example of something that will need to be fixed. I'm hoping it doesn't take much modification of what I already have.

At this point I think it would be useful to go through the pages I've already created and figure out which links are working and which are not, as I had run into a number of problems with this. When you find a good system, I'm hoping it won't be too bad to implement this for the functions, methods, and classes.

#### Links in `documentation/overview`
There are also links in `documentation/overview` that do not work. I would suggest using the aforementioned method to fix those, as there are a few links there that should link to other locations in the documentation.

### Automatically generating the toctrees
I'm not sure if this is something we'd need, but since I didn't imagine the documentation changing *that much*, I've manually inputted the pages into the toctrees of each `index.rst` file. So currently, if you were to have a new module all of a sudden, it should be created by `writeModFiles` (if you add it to the module list there – we may also want to automate that), and while that would create a new rst file in `documentation/modules`, you would need to add this manually to `documentation/index.rst`. So you could automate the creation of those toctrees, if you'd like.

### Other versions
I haven't done anything for different versions of metaknowledge (or thought much about how to handle this at all). I know that RTD has ways of handling versions of a package and the accompanying docs, so this might be something to consider, especially if people are still using older versions, or if newer versions are going to be released. I think RTD is supposed to handle this quite gracefully but it might involve some reworking of the docstrings in the previous versions.

### Other changes
#### Example notebooks
In addition to what still needs to be done with converting the docstrings, there are jupyter notebooks containing examples. Ideally, these will be converted by a script to RST or Markdown to be read by RTD as well, so that they will also be generated automatically if any changes are made to the notebooks. It would likely be easier to convert them to Markdown, but I'm not sure if you can use both Markdown and RST in the same RTD project; I think you might be able to though. T

Either way, I would talk to John about these notebooks to make sure they should be included, before diving into converting them.

#### Subtitles in table of contents/toctree
The original docs contain subtitles under each heading, and I think it would be cool to be able to include those subtitles with the entires in the toctree, but without those entries being hyperlinks. I've tried that using entries (http://www.sphinx-doc.org/en/stable/markup/toctree.html?highlight=entries), but I don't really like the look of it, so I removed it. Might be something to explore, but is fairly minor.

#### Simplifying the scripts
Simplify the scripts that generate the docs bc a lot of it is repeated or similar. (By the time you read this you may have already done so after looking at my not-so-efficient code.)

#### Delete the CLI pages?
I've been told that the CLI page is no longer necessary, confirm this and then delete CLI.rst. You'll need to delete any links to this page in the other page's toctrees too – though the errors will remind you of this if you forget.

If you're getting rid of this, remove it from `documentation/example`. If you're keeping it, fix the link there.

## Helpful links:
<a href="http://www.sphinx-doc.org/en/1.5.1/markup/toctree.html">Toc Tree syntax</a>

<a href="http://greentreesnakes.readthedocs.io/en/latest/nodes.html
">AST Module</a>

<a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html">reStructuredText</a>

<a href="https://stackoverflow.com/questions/15394347/adding-a-cross-reference-to-a-subheading-or-anchor-in-another-page">How to link to sections with RST</a>
