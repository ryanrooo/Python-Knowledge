import os
import sys

location1 = ''
location2 = ''

numbers = [1, 2, 3, 4, 5, 6]

def speechCount():
    list_of_sets = [418, 419, 420]

    for sets in list_of_sets:
        speechCount = 0
        data_path = cosmos + 's' + str(sets) + '-qa-ar0144-0-lip_reading/Data/'
        for folders in os.listdir(data_path):
            image_path = os.listdir(data_path + folders)
            for image in image_path:
                if image.endswith('.png'):
                    speechCount = speechCount + 1
        print sets, speechCount


def kpiCount():
    KPI_Count = 0
    total = 0
    kpi_sets = map(int, raw_input('Set #? ').split())
    for sets in kpi_sets:
        kpi_data = cosmos + 's' + str(sets) + "-eoc-1" + '/Data/'
        for user in os.listdir(kpi_data):
            if user.startswith('user'):
                data = os.listdir(kpi_data + user)
                for png in data:
                    if png.endswith('.png'):
                        total = total + 1
                        KPI_Count = KPI_Count + 1
        print str(sets) + ': ' + str(KPI_Count)
        KPI_Count = 0
    print 'Total: ' + str(total)


def WholeSetCount():
    list_of_sets = map(int, raw_input('Set #? ').split())
    WholeCount = 0
    total = 0

    for sets in list_of_sets:
        for j in numbers:
            data_path = cosmos2 + 's' + str(sets) +"-gaze-" + str(j) + '/Data/'
            for folders in os.listdir(data_path):
                if folders.startswith('T'):
			if folders.startswith('S'):
                   	 data = os.listdir(data_path + folders)
                   	 for png in data:
                        	if png.endswith('png'):
                            	WholeCount = WholeCount + 1
                            	total = total + 1
        print str(sets) + ': ' + str(WholeCount)
        WholeCount = 0
    print 'Total: ' + str(total)

def s_lip_count():
    list_of_sets = map(int, raw_input('Set #? ').split())
    s_lip = 0
    total = 0
    for sets in list_of_sets:
        data_path = cosmos + 's' + str(sets) + '-lip/'
        for user in os.listdir(data_path):
            user_path = data_path + user
            for video in os.listdir(user_path):
                png_path = data_path + user + '/' + video
                for data in os.listdir(png_path):
                    if data.endswith('.png'):
                        s_lip = s_lip + 1
                        total = total + 1
        #
        print str(sets) + ': ' + str(s_lip)
        s_lip = 0
    print 'Total: ' + str(total)


                    # data_count = len(os.listdir(data_path + folders + '/' + data))
                    # print data, data_count


if __name__ == "__main__":
    a = raw_input('K: for KPI_Count\nS: for SpeechCount\nW: for WholeSetCount\nL: for S-lip_Count\n  for ar0144\n')
    if a.lower() == 'k':
        kpiCount()
    if a.lower() == 's':
        speechCount()
    if a.lower() == 'w':
        WholeSetCount()
    if a.lower() == 'l':
        s_lip_count()

