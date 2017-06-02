#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""Python script to create customed colorbar.
"""
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# Python script written by Bin Xu (xubinrun@gmail.com)


import matplotlib.pyplot as plt
import argparse
import sys
import time
import numpy as np
from matplotlib import cm


def main():
    # Time start
    start_ticks = time.time()

    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__,
            epilog= """This is some addition description.
                    """)
    parser.add_argument("-nt","--notime", help="Don't dispaly time usage.", action="store_true", default=False)
    parser.add_argument("-k","--key", help="Define the key column.", type=int, default=1, metavar='col_num', nargs='+')
    parser.add_argument("-n","--nticks", help="Define the number of ticks.", type=int, default=6)
    parser.add_argument("-r","--range", help="Define the range of ticks.", default=(0.01, 0.3),type=float, nargs=2)
    parser.add_argument("-c","--cmap", help="Define the name of colormaps.", default='jet')
    parser.add_argument("-o","--outfile", help="Define the output file.", default='color_bar.png')
    args = parser.parse_args()

    # Your main process
    gradient = np.linspace(1,0,256)
    data = np.vstack((gradient,gradient))
    data= np.transpose(data)
    fig, axes = plt.subplots(figsize=(1,6))
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.1, right=0.26)
    axes.imshow(data,aspect='auto',cmap = plt.get_cmap(args.cmap))

    num = np.linspace(args.range[1],args.range[0],args.nticks,endpoint=True)
    position = np.linspace(0,255,args.nticks,endpoint=True)
    ylables = []
    for tmp in num:
        ylables.append("%.3f"%tmp)
        plt.yticks(position,ylables,fontsize=15)
    axes.yaxis.tick_right()
    axes.get_xaxis().set_visible(False)
    plt.savefig(args.outfile,transparent=False)

    # Time end
    end_tickes = time.time()
    # Output time usage
    if not args.notime:
        print "Time usage: %f s" % (end_tickes-start_ticks)
    return 0
    
if __name__ == "__main__":
    sys.exit(main())

