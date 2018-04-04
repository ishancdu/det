from scipy import misc
import numpy as np
import tensorflow as tf
import cv2
import detect_face


with tf.Graph().as_default():
    sess=tf.Session()
    with sess.as_default():
        pnet,rnet,onet=detect_face.create_mtcnn(sess,None)

minsize = 20
threshold = [ 0.6, 0.7 ,0.7 ]
#factor = 0.709
factor = 0.600

#image=cv2.imread("img.jpg")

cap = cv2.VideoCapture(0)

#while(True):
a=0
while(cap.isOpened()):
    a=a+1
    ret, image = cap.read()
    bounding_boxes, yes = detect_face.detect_face(image, minsize, pnet, rnet, onet, threshold, factor)
    print ("the no of faces are",len(bounding_boxes),len(yes))
    print ("the landmarks are ", yes)
    print ("the shape[0] is ", bounding_boxes.shape[0])
    print ("the bounding_boxes[:,0:4] is ", bounding_boxes[:,0:4])
    print ("the boxes are",bounding_boxes)
    '''
    nrof_faces = bounding_boxes.shape[0]
    if nrof_faces>0:
        det = bounding_boxes[:,0:4]
        det_arr = []
        img_size = np.asarray(image.shape)[0:2]
        if nrof_faces>1:
            bounding_box_size = (det[:,2]-det[:,0])*(det[:,3]-det[:,1])
            img_center = img_size / 2
            offsets = np.vstack([ (det[:,0]+det[:,2])/2-img_center[1], (det[:,1]+det[:,3])/2-img_center[0] ])
            offset_dist_squared = np.sum(np.power(offsets,2.0),0)
            index = np.argmax(bounding_box_size-offset_dist_squared*2.0) # some extra weight on the centering
            det_arr.append(det[index,:])
        else:
            det_arr.append(np.squeeze(det))

        for i, det in enumerate(det_arr):
            det = np.squeeze(det)
            bb = np.zeros(4, dtype=np.int32)
            bb[0] = np.maximum(det[0]-44/2, 0)
            bb[1] = np.maximum(det[1]-44/2, 0)
            bb[2] = np.minimum(det[2]+44/2, img_size[1])
            bb[3] = np.minimum(det[3]+44/2, img_size[0])
            cropped = image[bb[1]:bb[3],bb[0]:bb[2],:]
            scaled = misc.imresize(cropped, (182, 182), interp='bilinear')
            #nrof_successfully_aligned += 1
            #filename_base, file_extension = os.path.splitext(output_filename)
            
            if args.detect_multiple_faces:
                output_filename_n = "{}_{}{}".format(filename_base, i, file_extension)
            else:
                output_filename_n = "{}{}".format(filename_base, file_extension)
            misc.imsave(output_filename_n, scaled)
            text_file.write('%s %d %d %d %d\n' % (output_filename_n, bb[0], bb[1], bb[2], bb[3]))
        
    print ("the bb is ",bb)
    cv2.rectangle(image,(bb[0],bb[1]),(bb[2],bb[3]),(245,46,43),4)
    cv2.imshow("imageaa", image)
    '''
    for i in range(0,len(bounding_boxes)):
        #cv2.rectangle(image,((int(bounding_boxes[i][0])*2),(2*int(bounding_boxes[i][1]))),(2*(int(bounding_boxes[i][2])),(2*int(bounding_boxes[i][3]))),(245,46,43),4)
        cv2.rectangle(image,(int(bounding_boxes[i][0]),int(bounding_boxes[i][1])),(int(bounding_boxes[i][2]),int(bounding_boxes[i][3])),(245,46,43),4)
        for j in range(0,5):
            cv2.circle(image,(int(yes[j][i]),int(yes[j+5][i])),2,(0,0,255),4)

    print ("the frame no is ", a)
    cv2.imshow("image", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #print ("the bounding boxes are",len(bounding_boxes),yes,len(bounding_boxes[:,0:4]),bounding_boxes[0][1],int(bounding_boxes[1][1]))
        
cap.release()
cv2.destroyAllWindows()



'''
image=cv2.imread("img.jpg")
bounding_boxes, yes = detect_face.detect_face(image, minsize, pnet, rnet, onet, threshold, factor)

for i in range(0,len(bounding_boxes)):
    cv2.rectangle(image,(int(bounding_boxes[i][0]),int(bounding_boxes[i][1])),(int(bounding_boxes[i][2]),int(bounding_boxes[i][3])),(245,46,43),4)

    for j in range(0,5):
        cv2.circle(image,(int(yes[j][i]),int(yes[j+5][i])),2,(0,0,255),4)

print("no of faces are  ",len(bounding_boxes),len(yes))
print ("the landmarks are ", yes)
cv2.imshow("image", image)

cv2.waitKey(0)
'''
