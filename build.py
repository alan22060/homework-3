pages = [ 
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
}, 
{
           "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "contact me",
}, 
{

for page in pages:
    print(pages)

    # Read in the entire template
    template = open("base.html").read()
    # Read in the content of the index HTML page
    index_content = open(page["filename"]).read()
    # Use the string replace
    finished_index_page = template.replace("{{content}}", index_content)
    open("docs/about.html", "w+").write(finished_index_page)


def main():
 


    print('Building our static site')

    #Reads in the top.html
    print('Readin in html variables')
    top_html = open('./templates/top.html').read()


    #Reads in the botton.html
    botton_html = open('./templates/bottom.html').read()

    #Reads in the middle index.html

    middle_html = open('./content/index.html').read()

    print('combining HTML')
    combined_html = top_html +  middle_html + botton_html
    print(combined_html)

     def print(content):
     TODO: Read in template, do string replacing, and return result return results
     def main():
        content = open(’docs/index.html’).read()
        resulting_html_for_index = apply_template(content)

        def print(templates):
     TODO: Read in template, do string replacing, and return result return results
     def main():
        content = open(’docs/bottom.html’).read()
        resulting_html_for_index = apply_template(content)

        def print(top.html):
     TODO: Read in template, do string replacing, and return result return results
     def main():
        content = open('docs/top.html').read()
        resulting_html_for_index = apply_template(content)


    #Reads in the middle index.html

    open('./docs/index.html').write(combined_html)
main()