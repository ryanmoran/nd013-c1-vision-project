# Project overview

This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

# Dataset

## Dataset analysis

From a random sampling of the images included in the dataset, we can see that there are scenes taking place in urban and suburban locations, in night and day, and with varying weather.

![Random Sample](./assets/random-sample.png)

The dataset also includes a set of groundtruth classes. From the graph below, we can see that the objects classified in the dataset are mostly cars, with some pedestrians, and relatively few bicyclists.

![Class Distribution](./assets/class-distribution.png)

Furthermore, we can see that most images in the dataset contain between 10-30 labelled bounding boxes, with a smaller proportion containing more, up to more than 70 in a small number of instances.

![Box Count Distribution](./assets/box-count-distribution.png)

Looking at the distribution of the sizes of these boxes, we can see that most of them are smaller, but there are some boxes that consume nearly the entire image.

![Box Size Distribution](./assets/box-size-distribution.png)

An example of this type of large box might be a bus passing in front of the camera.

![Bus Example](./assets/bus-example.png)

Finally, as we saw from the random sampling, the dataset includes scenes from different times of day. The distribution below helps to show that most images are from relatively bright daytime scenes, but that there is also a smaller cluster of scenes taking place in dark conditions, likely nighttime scenes.

![Image Brightness Distribution](./assets/image-brightness-distribution.png)

## Cross validation

This section should detail the cross validation strategy and justify your approach.

# Training
## Reference experiment

This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

## Improve on the reference

This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
