# Stich all the files in the out_summarized directory into one file 
# and save it as summary.txt

# Import the os module
import os

# Iterate over the files in the out_summarized directory
for file in os.listdir('out_summarized'):
    # Open the file
    with open('out_summarized/' + file, 'r', encoding='utf-8') as f:
        # Read the file
        text = f.read()
        # Append the text to the summary.md file
        with open('summary.md', 'a', encoding='utf-8') as f:
            # Parse the title in file name
            title = ' '.join(file.split('.')[0].split('-'))
            # Add the title and the url to the text in markdown format
            f.write(title.capitalize() + '\n')
            f.write('https://thebootstrappedfounder.com/' + file.split('.')[0] + '/\n')
            f.write(text)
            f.write('\n \n')
