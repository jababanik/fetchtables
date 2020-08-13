<h1> Project description </h1>
<h2> The fetchtables package </h2>
Extraction of table values from an image.
<h2> How to install </h2>
pip install fetchtables
<h3> Windows </h3>
Windows users will have to build or download poppler for Windows. You will then have to add the bin/ folder to PATH or use poppler_path = r"C:\path\to\poppler-xx\bin" as an argument in convert_from_path. <br>
<h3> For anaconda : </h3> conda install -c conda-forge poppler
<h2> How does it work? </h2>
<h3> Function fetchtables() </h3>
Returns an object of fetchtable :
<pre>
>>> import fetchtables as ft
>>> text = ft.getTable(image, show)	<br>
</pre>
OR <br>
<pre>
>>> fetchtable(image, show).to_csv(csv_file_name) <br>
</pre>
Image will be path of the image along with image name or numpy array of image.
<h2> Here are the definitions for feature tuning: </h2>
<h3> Grayscale_threshold:</h3> Default value is 180. If the outline of the table is lighter in shade, increase the value to get better result at identifying the table border.
<h3> get_tables(Min_Yaccess_Bias = True, show = True): </h3> Min_Yaccess_Bias defines the shortest y-axis value acceptable for the given table border. If show is True,image is shown. 
<h3> canny _ threshold 1 = 50, canny _ threshold2 = 150: </h3>
<h3> HL = huelines threshold = 200 </h3>
<h3> Hough lines: Minimum lenght parameter </h3> The default value of huelines min line length = 500
Hough Transform is a popular technique to detect any shape, if you can represent that shape in mathematical form. It can detect the shape even if it is broken or distorted a little bit. <br>
<code>
  lines = cv2.HoughLines(edges,1,np.pi/180,200)
</code>
cv2.HoughLines(). It simply returns an array of (\rho, \theta) values. \rho is measured in pixels and \theta is measured in radians. First parameter, Input image should be a binary image, so apply threshold or use canny edge detection before finding applying hough transform. Second and third parameters are \rho and \theta accuracies respectively. Fourth argument is the threshold, which means minimum vote it should get for it to be considered as a line. Remember, number of votes depend upon number of points on the line. So it represents the minimum length of line that should be detected.

<h3> huelines max line gap =20 </h3>
