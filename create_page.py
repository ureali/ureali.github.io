# Program Name: Page Generator
# Program Purpose: Generate blog posts from template
# Author: Stanislav Nehretskyi
# Date last modified: 1/26/2024

from bs4 import BeautifulSoup;

# Define variables
postName = input('Please type the name of the post: ')
postTitle = input('Please type the title of the post: ')
destination = f'blog/{postName}.html'


# Copy and paste html from the template
def copy_html(source_file, destination_file,):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as source:
            # Read the HTML content from the source file
            html_content = source.read()
            html_content = html_content.replace('post_title', postTitle)

            # Open the destination file in write mode
            with open(destination_file, 'w') as destination:
                # Write the HTML content to the destination file
                destination.write(html_content)

        print(f'HTML code copied from {source_file} to {destination_file} successfully.')

    except FileNotFoundError:
        print("File not found. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Add link to the new post to blog index
def add_to_blog_list(destination_file):
    try:
        with open(destination_file, 'r') as source:
            # Create li and a elements
            blog_index = source.read()
            soup = BeautifulSoup(blog_index)
            index_li = soup.new_tag('li')
            index_link = soup.new_tag('a', href=f"{postName}.html")
            index_link.string = postTitle
            # Insert the elements to the documents
            soup.body.main.nav.ul.insert(0, index_li)
            soup.body.main.nav.ul.li.append(index_link)

        with open (destination_file, 'w') as destination:
            destination.write(soup.prettify(formatter='html'))
                                            
    except FileNotFoundError:
        print("File not found. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    print('Blog index updated sucessfully!')

copy_html('template.html', destination)
add_to_blog_list('blog/blog.html')