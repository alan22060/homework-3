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

#Reads in the middle index.html

middle_html = open('./content/index.html').read()