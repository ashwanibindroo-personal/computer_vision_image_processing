#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Importing necessary Libraries
from PIL import Image


# In[39]:


#Define the variable to store and open the image
im = Image.open("Home to pak.png")
im


# In[40]:


#Print the format, size and mode of the image
print(im.format, im.size, im.mode)


# In[41]:


#Open the image in the inbuilt utility
im.show()


# In[42]:


#convert the files to JPEG
import os, sys

for infile in sys.argv[1:]:
    f,e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)


# In[43]:


#create JPEG thumbnails
size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)


# In[44]:


#Identify image files
for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass


# In[45]:


infile


# In[46]:


#copying a subrectangle from the image
box = (100, 100, 400, 400)
region = im.crop(box)


# In[47]:


region


# In[48]:


#processing a subrectangle and pasting it back
region = region.transpose(Image.Transpose.ROTATE_180)
im.paste(region, box)


# In[49]:


region


# In[ ]:




