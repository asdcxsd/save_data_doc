import serial
import time

z1baudrate = 115200  # toc do
z1port = '/dev/ttyUSB0'  # cong
file_save = "input_goc_GPS01.in"
file_name_excel = "test.xls"

import xlwt
import xlrd
from xlwt import Workbook
from xlutils.copy import copy

def save_to_excel(name_file, data):
    try:
        r = 0
        try:
            rb = xlrd.open_workbook(name_file,formatting_info=True)
            r_sheet = rb.sheet_by_index(0)
            r = r_sheet.nrows
        except:
            wb = Workbook()
            sheet1 = wb.add_sheet('Sheet1')
            wb.save(name_file)
            print "create file"
            save_to_excel(name_file, data)

            return
        wb = copy(rb)
        sheet = wb.get_sheet(0)
        # ------------------------
        data = data.split('\r\n')
        for i in data:
            sheet.write(r,0,i) # gi vao row, col
            r = r+ 1
        #---------------------------
        wb.save(name_file)
    except Exception as e:
        print e




try:
    z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
    z1serial.timeout = 2  # set read timeout
    # print z1serial  # debug serial.
    print z1serial.is_open  # True for opened
    if z1serial.is_open:
        while True:
            size = z1serial.inWaiting()
            if size:
                data = z1serial.read(size)
                file = open(file_save, 'a')
                #save_to_excel(file_name_excel, data)
                print data
                file.write(data)
                print 'OK'
                file.close();
            time.sleep(1)
    else:
        print 'z1serial not open'
except:
    print 'Error'
