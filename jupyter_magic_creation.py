from enum import Enum
import pandas as pd
from io import StringIO
import time

from IPython.core.display import display, HTML
from IPython.core.magic import Magics, magics_class, cell_magic, line_magic, \
    needs_local_scope, register_cell_magic
from IPython.core.magic_arguments import argument, magic_arguments, \
    parse_argstring
from hdfs3 import HDFileSystem

horton = HDFileSystem(host='horton')
stampy = HDFileSystem(host='stampy')
tahoe = HDFileSystem(host='tahoe')


@magics_class
class mymagics(Magics):

    @register_cell_magic
    @magic_arguments()
    #     @line_magic
    #     @cell_magic
    @argument("-s", "--save", type=str, help="dataframe to be saved into csv format")
    def cdataframe(line, cell):

        sio = StringIO(cell)
        data = pd.read_csv(sio)
        return data

        if args.save:
            sio = StringIO(cell)
            data = pd.read_csv(sio)
            sv = data.to_csv(args.save)

            return data

    @magic_arguments()
    @line_magic
    @cell_magic
    @argument("-d", "--download", type=bool, default=False,
              help="True to download data")
    @argument("-s", "--save", type=str, help="Local file name to be loaded ")
    @argument("-r", "--read", type=str, help="read local text file")
    @argument("--text", type=str, help="the text to write to the file")
    def savetext(self, arg, line='', cell='', local_ns={}):
        """Connects to hive execution engine of garfield cluster for query
        execution.

        Example1:

        %save -s text.txt --text "text to go into a text file"

        """
        # save globals and locals so they can be referenced in bind vars
        if len(line) == 0 and len(cell) == 0:
            if not arg.startswith("-"):
                line = arg
                arg = ''
        args = parse_argstring(self.savetext, arg)

        if cell is None or len(cell) == 0:
            cell = line

        if args.save and args.text:
            print("writing below to file: " + str(args.text) + " to -->" + str(args.save))
            doc = open(args.save, 'w')
            doc.write(args.text)
            doc.close()

        if args.read:
            doc = open(args.read, "r")
            print(doc.read())

    @magic_arguments()
    @line_magic
    @cell_magic
    @argument("-o", "--open", type=str, help="Local CSV file name to be loaded")
    @argument("-d", "--dataframecol", type=str, help="dataframe a csv column")
    def csv(self, arg, line='', cell='', local_ns={}):


        if len(line) == 0 and len(cell) == 0:
            if not arg.startswith("-"):
                line = arg
                arg = ''
        args = parse_argstring(self.csv, arg)

        if cell is None or len(cell) == 0:
            cell = line

        if args.open and args.dataframecol:
            data = pd.read_csv(args.open)
            frame = data[args.dataframecol]
            print(frame)

    @magic_arguments()
    @argument("-u", "--usage", action="store_true", help="print the storage usage results")
    @argument("-hs", "--horton_stampy", action="store_true", help="print the storage usage results")
    @argument("-ht", "--horton_tahoe", action="store_true", help="print the storage usage results")
    @argument("-st", "--stampy_tahoe", action="store_true", help="print the storage usage results")
    @argument("-mydir", "--mydirectory", type=str, help="lists your directory")
    @cell_magic
    @line_magic
    def usage(self, arg, line='', cell=''):
        """Example1:


          ***displays Horton, Stampy, and Tahoe storage***

            %status -u

           ***Comapares Horton and Stampy***

           %status -hs

           ***Compares Horton and Tahoe***

           %status -ht

           ***Compares Stampy and Horton***

           %status -st

        """
        hor = (horton.df())
        stam = (stampy.df())
        tah = (tahoe.df())
        args = parse_argstring(self.usage, arg)

        if args.usage and args.mydirectory:
            print("This will check the current storage of hive storage systems")
            print("Horton: ")
            print(hor)
            print("\n")
            print("Files in Horton server: ")
            print(horton.ls("/user/" + args.mydirectory))
            print("\n")
            time.sleep(1)

            print("Stampy:")
            print(stam)
            print("\n")
            print("Files in Stampy server: ")
            print(stampy.ls("/user/" + args.mydirectory))
            print("\n")
            time.sleep(1)

            print("Tahoe:")
            print(tah)
            print("\n")
            print(tahoe.ls("/user/" + args.mydirectory))

        if args.horton_stampy:
            print("Horton: ")
            print(horton.df())
            time.sleep(1)
            print("Stampy:")
            print(stampy.df())

        if args.horton_tahoe:
            print("Horton: ")
            print(horton.df())
            time.sleep(1)
            print("Tahoe: ")
            print(tahoe.df())

        if args.stampy_tahoe:
            print("Stampy: ")
            print(stampy.df())
            time.sleep(1)
            print("tahoe: ")
            print(tahoe.df())



def load_ipython_extension(ip):
    #     """Load the PPMagics extension in IPython."""
    #     js = "IPython.CodeCell.options_default.highlight_modes[""'magic_text/x-sql'] = {'reg':[/^.*%%?.*/""]};"
    #     display_javascript(js, raw=True)
    ip = get_ipython()
    ip.register_magics(PPMagics)


ip = get_ipython()
ip.register_magics(mymagics)