# Program Name: Page Generator
# Program Purpose: Generate blog posts from template
# Author: Stanislav Nehretskyi
# Date last modified: 1/26/2024

# Note:
# ChatGPT was used to assist me in writing this
# It provided the base code, I fixed the bugs, and modified it for my needs

def copy_html(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as source:
            # Read the HTML content from the source file
            html_content = source.read()

            # Open the destination file in write mode
            with open(destination_file, 'w') as destination:
                # Write the HTML content to the destination file
                destination.write(html_content)

        print(f"HTML code copied from {source_file} to {destination_file} successfully.")

    except FileNotFoundError:
        print("File not found. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

postName = input('Please type the name of the post: ')
destination = f'blog/{postName}.html'
copy_html('template.html', destination)