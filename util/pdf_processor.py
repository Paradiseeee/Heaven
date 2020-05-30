# -*- coding: utf-8 -*-

import PyPDF2 as pp


class PDFProcessor():
    '''实现预览、拆分、合并三个功能'''

    def __init__(self):
        '''Initializing'''

        PATH = input(">>>请输入源文件所在目录：\n")
        TYPE = input(">>>请选择操作类型：_预览（1）_|_拆分（2）_|_合并（3）_\n")

        FILENAMES, FILENAME, PAGES = None, None, None
        if TYPE == '3':
            temp = input(">>>请输入要合并的文件（两个或多个，用逗号隔开）：\n")
            FILENAMES = [f.strip() for f in temp.split(',')]
        elif TYPE == '2':
            FILENAME = input(">>>请输入要提取的文件名：\n")
            temp = input(">>>请输入需要获取的页码（从第一页数起，用逗号隔开）：\n")
            PAGES = [int(p.strip()) for p in temp.split(',')]
        else:
            FILENAME = input('>>>请输入要预览的文件名：\n')

        OUTPUT_PATH, OUTPUT = None, None
        if TYPE in ['2', '3']:
            OUTPUT_PATH = input(">>>指定输出的路径（含文件名）：\n")

        self.PATH = PATH
        self.TYPE = TYPE
        self.FILENAMES = FILENAMES
        self.FILENAME = FILENAME
        self.PAGES = PAGES
        self.OUTPUT_PATH = OUTPUT_PATH


    def main(self):
        '''流程控制'''
        if self.TYPE == '1':
            self.extract_information(self.PATH + self.FILENAME)
        elif self.TYPE == '2':
            self.split_pdfs(self.OUTPUT_PATH, self.PATH + self.FILENAME, self.PAGES)
        elif self.TYPE == '3':
            self.merge_pdfs(self.OUTPUT_PATH, self.PATH, self.FILENAMES)


    def extract_information(self, filepath):
        ''' 这里函数结束之后文件关闭，无法调用.extractText方法读取文本'''
        with open(filepath, 'rb') as f:
            pdf = pp.PdfFileReader(f)
            information = pdf.getDocumentInfo()
            pages = pdf.getNumPages()
            print('\n提取信息如下：\n')
            for key, value in information.items():
                print(f'{key}: \t{value}')

            return pdf, information, pages
    

    def merge_pdfs(self, outputpath, filepath, filenames):
        '''将filepaths中的文件合并，并写入outputpath'''
        writer = pp.PdfFileWriter()
        filepaths = [filepath + n for n in filenames]
        for path in filepaths:
            pdf = pp.PdfFileReader(path)
            for page in range(pdf.getNumPages()):
                writer.addPage(pdf.getPage(page))
        with open(outputpath, 'wb') as f:
            writer.write(f)
        print('成功写出文件！')
    

    def split_pdfs(self, outputpath, filepath, pages):
        '''提取页码为pages的页，输出为新文件'''
        writer = pp.PdfFileWriter()
        pdf = pp.PdfFileReader(filepath)
        for p in pages:
            if p > pdf.getNumPages():
                print(f'页数<{p}>超出文档页码范围！')
            else:
                page = pdf.getPage(p-1)
                writer.addPage(page)
        with open(outputpath, 'wb') as f:
            writer.write(f)
        print('成功写出文件！')


if __name__ == '__main__':

    processor = PDFProcessor()
    processor.main()