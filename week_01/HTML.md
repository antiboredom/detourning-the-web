#HTML & CSS


## HTML
HTML is made up of elements. Elements are made of tags. 

Most tags look like this

```html
<tagname>some content goes here</tagname>
```

Most elements have an opening tag, some content, and then a closing tag.

Here's a paragraph tag:

```html
<p>I'm a paragraph</p>
```

Different tags are used for different types of content:

* ```p```: paragraph of text
* ```a```: a link
* ```ul``` : unordered (bulleted) list
* ```li```: a list item
* ```strong```: important text
* ```h1```: A large headline
* ```h2```: A smaller headline
* ```div```: a widely used tag to signify a division or section of content


### Attributes

Tags can also have **attributes**. These are key/value pairs that declare extra information about the tag. An attribute looks like this:

```html
<tagname attributename="value">content</tagname>
```

Some attributes can be applied to any tag. The two most important ones (for our purposes) are ```id``` and ```class```.

The ```id``` attribute gives a **unique** id to a tag. There can only by **one** tag with any given ```id```.

```html
<p id="the-most-important-paragraph">This is the most important paragraph.</p>
```

The ```class``` attribute indicates a user-defined category for a tag. Many tags (including different types of tags) can share the same class name.

```html
<p class="sort-of-important">I'm a sort of important paragraph</p>

<p class="sort-of-important">I'm also a sort of important paragraph</p>

<p class="sort-of-important">I'm another a sort of important paragraph</p>
```


Some attributes are specific to certain tags.

The ```a``` tag, for example, requires an ```href``` attribute that indicates where the browser should navigate to one someone clicks on it.

```html
<a href="http://whitehouse.gov">don't click here</a>
```

Some tags DON'T have a closing tag. The image tag, for example, doesn't have a closing tag but requires the ```src``` attribute to be set:

```html
<img src="lolcapitalism.jpg">
```

### A Barebones Webpage

All HTML documents contain the following tags:

* ```html```: Surrounds the entire document
* ```head```: A tag that doesn't render to the page but contains important links to style sheets and the title tag
* ```title```: The title of the page
* ```body```: Surrounds the body of the page


HTML elements are nested within other elements.

For example, here's a complete HTML document:

```html
<html>
	<head>
		<title>My Cool Website</title>
	</head>
	<body>
		<div>
			<h1>A Communisty Manifesto</h1>
			
			<p>Many <strong>spectres</strong> are haunting Europe. Here are some of them:</p>
			
			<ul>
				<li>The first spectre</li>
				<li>The second spectre</li>
				<li>The third spectre</li>
			</ul>
			
			<p>Keep reading to find out all of the spectres currently haunting Europe!</p>
		</div>
	</body>
</html>
```

Note the indentations. These are completely optional (the machine doesn't care if you indent or not), but it's good practice to always indent elements inside of other elements because it helps show the structure of the document.

##CSS

CSS stands for "cascading stylesheet". It's a language for giving style/design to HTML. The particulars of CSS styling are irrelevant for this class. What matters for us is the syntax CSS uses because it provides a handy system for isolating and extracting particular elements from an HTML document. To apply css, you use CSS selectors.

We can style every instance of a tag by referencing the name of the tag:

```css
p {
	color: red;
}
```

Style a tags that are INSIDE p tags:

```css
p a {
	background-color: black;
}
```

Importantly, we can also give style to tags that have particular ids or classes.

You can select classes by preceding the class name with a period ```.``` character.

Style all tags with the "proletariat" class:

```css
.proletariate {
	background-color: red;
}
```

Select ids by preceding the id name with a hashtag ```#``` character.

```css
#the-manifesto {
	border: 10px solid orange;
}
```

###Here's a more complete list of css selectors: [http://www.cheetyr.com/css-selectors](http://www.cheetyr.com/css-selectors). 


## Isolating Elements with CSS Selectors

Our goal is to extract data from HTML documents. To do this we can grab elements with CSS selectors, or using another technique called xpath (which I'll cover later).

To get started we can use the javascript console in Chrome or Firefox. Open up the console, and then type the following:

```javascript
document.querySelectorAll("selectorname")
```

Replace "selectorname" with whatever you're looking for.

```javascript
document.querySelectorAll("a") 			// gets all the links
document.querySelectorAll("p") 			// gets all the paragraph tags
document.querySelectorAll('.product') 	// gets every tag with the class "product"
document.querySelectorAll('.product a') // gets every link inside tags with the class "product"
document.querySelector("#article-name") // gets the tag with id "article-name"
```








