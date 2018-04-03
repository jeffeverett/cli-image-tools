# cli-image-tools
Collection of small command-line tools to work with images.

## imresize
Resizes images to specified size.

### Usage:
```{r}
./imresize files target_width target_height
```
where *files* is a list of one-or-more file system objects, *target_width* is either an integer specifying the desired width in pixels or a float specifying the scaling factor for the width, and *target_height* is the same as *target_width* but for the height dimension.

## im2gray
Converts color images to grayscale.

### Usage:
```{r}
./im2gray files
```
where *files* is a list of one-or-more file system objects.

## imshape
Prints the dimensions of the image in the format (*height*,*width*,*depth*).

### Usage:
```{r}
./imshape files
```
where *files* is a list of one-or-more file system objects.
