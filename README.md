# Install
```
pip install -r requirements.txt
```

# Run
```
make clean
python main.py
```

# About
Two part Python coding challenge. 

## Part 1 - Image generation
First part involves generating images for the 12 days of Christmas. This code is in the `dozen_days_generator` folder. Each day gets an image with a different number of common objects in the image. We are using `cvlib` which has an API for detecting common objects using the **YOLOv3** model. This model has a list of ~80 common objects. We scrape the web for those search terms (using Bing's search APIs) and pull down a handful of images for each search term. Then we do some image manipulation to ensure we have the correct number of objects based on the day.

## Part 2 - Image detection
Second part involves getting a set of 12 randomly labeled images and classifying them according to what day they represent. We do this by running a image classification from `cvlib` and then we allocate each image into the days that they represent using a maximum bipartite matching. We use a bipartite matching because Part 2 does not know how the images in Part 1 are generated. For example, some nefarious actor could insert an image with 12 fire hydrants that has 2 trees in the background, another image in that set would have 2 horses. We want to assign the 12 fire hydrant image to day 12 and not day 2, because the 2 horse image would be assigned to day 2.

# Learnings
- Object detection
- networkx
- cvlib
