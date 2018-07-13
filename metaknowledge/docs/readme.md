Hi! If you're reading this it means you've been tasked with completing what I started to convert the metaknowledge docs to read the docs. (Or, you are me in a few weeks returning to work on this.) This should help you understand what I've done, what's left to be done, and how to do it.

If you have any questions, message me on mattermost or email me at rewood34@mgmail.com (will be more responsive here).

The existing docs for metaknowledge are <a href="http://networkslab.org/metaknowledge/documentation/metaknowledgeFull">here</a>.

## Setting up the docs for read the docs
I've been working from <a href="https://github.com/rachel94/metaknowledge">this cloned repo of metaknowledge</a>. If you need access to this, let me know. The scripts used to create the docs are in <a href="https://github.com/rachel94/metaknowledge/tree/master/metaknowledge/docs">metaknowledge/metaknowledge/docs</a>.

I started by doing <a href="https://docs.readthedocs.io/en/latest/getting_started.html">this tutorial</a> from Read the Docs. I opted to use reStructuredText simply because the tutorial for it seemed easier. If you'd rather use Markdown and think it won't be too difficult to change (or to use both together) feel free to do so. Following the tutorial and using `sphinx quickstart`, the following were created:
<li> \_build (this is where the generated html pages will go)
<li> \_static (So far this is empty. I assume this is where you'd put css or js if you needed it, though read the docs has built in styling that has mostly been sufficient. You might find a use for some additional styles though, so I think they'd go here)
<li> \_templates (this is also empty, I'm not sure what you'd put here)
<li> conf.py (this is an important file, I believe I changed all the necessary values within it)
<li> make.bat (this is needed to generate your html files)
<li> Makefile (this is needed to generate your html files)

I then added the following:
<li> readme.md (this file)
<li> index.rst (this is the main page of your docs on read the docs. the toctree is super important within it, and is explained in the above tutorial. Otherwise, you can put whatever content you want; so I put the intro text for metaknowledge on the old documentation)
<li> all the other files ending in .rst (these are the other pages at the top level of our read the docs file structure)
<li> all other subdirectories (these contain more pages that are on our read the docs, but that are nested)
<li> regex.txt (contains a list of some useful regular expressions I've been using to find and replace parts of the docstrings. You will likely end up creating more of these, but they speed things up a lot)

## Generating pages for read the docs
If you continue to use rst like I've been, you can learn the syntax <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html">here</a>. Some things are kind of annoying in rst, such as making a hyperlink italicized, because it doesn't allow for nested styles (which was super annoying). However, there are weird workarounds to this, where you sort of put in a variable, and then replace the variable later. Take a look at install.rst for some examples of this.

Or, if you're using markdown, use that syntax instead.

When you want to convet your rst pages to html to look like read the docs style, simply do the following on the command line:
`cd [wherever you stored this repo]/metaknowledge/metaknowledge/docs`
`make html`
This generates the html riles from the rst, and puts them in \_build. You can then view them in a browser by just opening the html pages.

## Getting the files live on read the docs
I've made a read the docs account where I'm hosting the docs right now, I mostly did this for learning purposes, but ultimately this will need to be hosted on a netlab account or something. You can still test what the files will look like on rtd just by opening the html files in a browser, so you don't *need* to make your own rtd account to do this.

But if you are the one putting the docs on rtd, essentially you do the following (there are more thorough tutorials online):
<li> make a <a href="https://readthedocs.org/">rtd</a> account
<li> go to the dropdown bestide your username in the top right corner and click 'My Projects'
<li> click 'Import a Project'
<li> click 'Import Manually'
<li> provide the url to your git repo where the docs are (I think your repo needs to be public to work with this)
<li> Now you also have to add a webhook in your repo on git or wherever it's hosted. This allows any new pushes to your repo to automatically push to read the docs too. So if you're using git hub, go to your repo's settings > WebHooks > Add webhook. For 'Payload URL', you put in the url that you can find on read the docs under Projects > your project (mk) > Admin > Integrations. There should be a link there that will say it can be used for incoming webhooks.
<li> Then if it hasn't built already, go to Projects / your project / Overview, and click Build.
<li> You can view the docs by clicking 'View Docs'
<li> When you make changes to your docs, make sure you run docsGen.py (see below), then run make html to remake the html pages, then push to git. This will automatically make the changes on read the docs.

## Understanding the docsGen.py script I wrote

## Converting the docstrings to work with rst

## What's left to do
In addition to what still needs to be done with docsGen.py, there are jupyter notebooks containing examples.

I've been told that the CLI page is no longer necessary, confirm this and then delete CLI.rst. You'll need to delete any links to this page in the other page's toctrees too.
