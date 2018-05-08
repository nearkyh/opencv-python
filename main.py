import sys
from utils import camshift, meanshift


CAM_ID = sys.argv[1]

if __name__ == '__main__':
	#camshift.camShift(CAM_ID)

	meanshift.meanShift(CAM_ID)

