# Date originally created: October 7, 2021
# Date finished: October 9, 2021 - 11:28 pm
# Created by: Zeri Aaron Malacas - 19 years old


# This program is used for getting the frequency distribution table automatically
# with up to two decimals in given values
# Features:
# Class Interval, Frequency, CM, f(CM), <cf
# Additional Features:
# Show Class Boundaries: Class Boundaries in another window
# Show Essentials:
# Lowest, Highest, Range, Number of rows, Class size, Xlb, fa, fm, fb, cumfb
# Mean, Median, Mode: Mean, Median, and Mode

from tkinter import *
import numpy as np
import math

# constant values
standard_addition_0 = 1
standard_addition_1 = 0.1
standard_addition_2 = 0.01

# constant class boundary value
const_0 = 0.5 # whole number
const_1 = 0.05 # 1 decimal
const_2 = 0.005 # 2 decimals


# START INPUTS

count_elements = int(input()) # count of values # int

decimal_count = int(input()) # decimal place # int



if decimal_count == 0:
    while True:
        elements = list(map(int, input().split()))
        elements = sorted(elements)
        if len(elements) == count_elements:
            break

    lowest = min(elements)
    highest = max(elements)

    range_c = highest - lowest

    specify_rows = input()
    if specify_rows.lower() == 'n':
        number_rows = round(1 + (3.3 * math.log10(count_elements)))
    elif specify_rows.lower() == 'y':
        number_rows = int(input())

    specify_interval = input()
    if specify_interval.lower() == 'n':
        actual_class_size = round(range_c / number_rows)
    elif specify_interval.lower() == 'y':
        actual_class_size = int(input())

    actual_lower_limit = []
    actual_upper_limit = []

    actual_limits = []

    actual_lower_class_bound = []
    actual_upper_class_bound = []

    actual_cm = []

    for i in range(number_rows):
        lower_limit = lowest + (actual_class_size * i)
        upper_limit = (lowest + (actual_class_size * (i + standard_addition_0))) - standard_addition_0
        actual_lower_limit.append(lower_limit)
        actual_upper_limit.append(upper_limit)

        limits = range(actual_lower_limit[i], (actual_upper_limit[i] + standard_addition_0))
        actual_limits.append(limits)

        lower_class_bound = actual_lower_limit[i] - const_0
        upper_class_bound = actual_upper_limit[i] - const_0
        actual_lower_class_bound.append(lower_class_bound)
        actual_upper_class_bound.append(upper_class_bound)

        cm = round((actual_lower_limit[i] + actual_upper_limit[i]) / 2, 2)
        actual_cm.append(cm)

    # Frequency
    freq1 = []
    freq2 = []
    freq3 = []
    freq4 = []
    freq5 = []
    freq6 = []
    freq7 = []
    freq8 = []
    freq9 = []
    freq10 = []
    freq11 = []
    freq12 = []
    freq13 = []
    freq14 = []
    freq15 = []
    freq16 = []
    freq17 = []
    freq18 = []
    freq19 = []
    freq20 = []
    freq21 = []
    freq22 = []
    freq23 = []
    freq24 = []
    freq25 = []
    freq26 = []
    freq27 = []
    freq28 = []
    freq29 = []
    freq30 = []

    try:
        for value in elements:
            if value in actual_limits[0]:
                freq1.append(value)
        for value in elements:
            if value in actual_limits[1]:
                freq2.append(value)
        for value in elements:
            if value in actual_limits[2]:
                freq3.append(value)
        for value in elements:
            if value in actual_limits[3]:
                freq4.append(value)
        for value in elements:
            if value in actual_limits[4]:
                freq5.append(value)
        for value in elements:
            if value in actual_limits[5]:
                freq6.append(value)
        for value in elements:
            if value in actual_limits[6]:
                freq7.append(value)
        for value in elements:
            if value in actual_limits[7]:
                freq8.append(value)
        for value in elements:
            if value in actual_limits[8]:
                freq9.append(value)
        for value in elements:
            if value in actual_limits[9]:
                freq10.append(value)
        for value in elements:
            if value in actual_limits[10]:
                freq11.append(value)
        for value in elements:
            if value in actual_limits[11]:
                freq12.append(value)
        for value in elements:
            if value in actual_limits[12]:
                freq13.append(value)
        for value in elements:
            if value in actual_limits[13]:
                freq14.append(value)
        for value in elements:
            if value in actual_limits[14]:
                freq15.append(value)
        for value in elements:
            if value in actual_limits[15]:
                freq16.append(value)
        for value in elements:
            if value in actual_limits[16]:
                freq17.append(value)
        for value in elements:
            if value in actual_limits[17]:
                freq18.append(value)
        for value in elements:
            if value in actual_limits[18]:
                freq19.append(value)
        for value in elements:
            if value in actual_limits[19]:
                freq20.append(value)
        for value in elements:
            if value in actual_limits[20]:
                freq21.append(value)
        for value in elements:
            if value in actual_limits[21]:
                freq22.append(value)
        for value in elements:
            if value in actual_limits[22]:
                freq23.append(value)
        for value in elements:
            if value in actual_limits[23]:
                freq24.append(value)
        for value in elements:
            if value in actual_limits[24]:
                freq25.append(value)
        for value in elements:
            if value in actual_limits[25]:
                freq26.append(value)
        for value in elements:
            if value in actual_limits[26]:
                freq27.append(value)
        for value in elements:
            if value in actual_limits[27]:
                freq28.append(value)
        for value in elements:
            if value in actual_limits[28]:
                freq29.append(value)
        for value in elements:
            if value in actual_limits[29]:
                freq30.append(value)
    except IndexError:
        pass

    len_freq1 = len(freq1)
    len_freq2 = len(freq2)
    len_freq3 = len(freq3)
    len_freq4 = len(freq4)
    len_freq5 = len(freq5)
    len_freq6 = len(freq6)
    len_freq7 = len(freq7)
    len_freq8 = len(freq8)
    len_freq9 = len(freq9)
    len_freq10 = len(freq10)
    len_freq11 = len(freq11)
    len_freq12 = len(freq12)
    len_freq13 = len(freq13)
    len_freq14 = len(freq14)
    len_freq15 = len(freq15)
    len_freq16 = len(freq16)
    len_freq17 = len(freq17)
    len_freq18 = len(freq18)
    len_freq19 = len(freq19)
    len_freq20 = len(freq20)
    len_freq21 = len(freq21)
    len_freq22 = len(freq22)
    len_freq23 = len(freq23)
    len_freq24 = len(freq24)
    len_freq25 = len(freq25)
    len_freq26 = len(freq26)
    len_freq27 = len(freq27)
    len_freq28 = len(freq28)
    len_freq29 = len(freq29)
    len_freq30 = len(freq30)

    initial_frequency = [len_freq1, len_freq2, len_freq3, len_freq4, len_freq5,
                         len_freq6, len_freq7, len_freq8, len_freq9, len_freq10,
                         len_freq11, len_freq12, len_freq13, len_freq14, len_freq15,
                         len_freq16, len_freq17, len_freq18, len_freq19, len_freq20,
                         len_freq21, len_freq22, len_freq23, len_freq24, len_freq25,
                         len_freq26, len_freq27, len_freq28, len_freq29, len_freq30]

    # frequency
    actual_frequency = [value for value in initial_frequency if value != 0]

    total_frequency = sum(actual_frequency)

    actual_fcm = []

    for i in range(number_rows):
        fcm = actual_frequency[i] * actual_cm[i]
        actual_fcm.append(fcm)

    total_fcm = sum(actual_fcm)

    actual_less_cf = []

    len_less_f = len(actual_frequency)
    for i in range(len_less_f):
        less_cf = sum(actual_frequency[:i + 1])
        actual_less_cf.append(less_cf)

    # fm, fb, fa, Xlb, and cumfb, class size

    # FM, FB, FA
    actual_fm = max(actual_frequency)  # modal class

    i_fm = actual_frequency.index(actual_fm)  # modal class

    i_fb = i_fm - 1
    i_fa = i_fm + 1

    actual_fb = actual_frequency[i_fb]

    actual_fa = actual_frequency[i_fa]

    # Xlb, cumfb
    actual_xlb = actual_lower_class_bound[i_fm]

    actual_cumfb = actual_less_cf[i_fb]

    # d1, d2
    actual_d1 = actual_fm - actual_fb
    actual_d2 = actual_fm - actual_fa

    # Mean, median, mode

    actual_mean = round(sum(elements) / count_elements, 2)

    actual_median = np.median(elements)

    actual_mode = round(actual_xlb + (actual_d1 / (actual_d1 + actual_d2) * actual_class_size), 2)


    # GUI Tkinter

    root = Tk()
    root.title("Frequency Distribution Table")
    root.resizable(0, 0)

    for i in range(number_rows):
        # Class Interval Plot
        label_class_interval = Label(root, width=20, text="Scores (Class Interval)", font=("Arial", 16), justify="center",
                                     bg="gray")
        entry_class_interval = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_class_interval.insert(END, actual_lower_limit[i])
        entry_class_interval.insert(END, " - ")
        entry_class_interval.insert(END, actual_upper_limit[i])
        label_class_interval.grid(row=0, column=0)
        entry_class_interval.grid(row=i + 1, column=0)


        def class_bound():
            top_class_bound = Toplevel()
            top_class_bound.resizable(0, 0)
            # Class Boundaries Plot
            for i in range(number_rows):
                label_class_boundaries = Label(top_class_bound, width=20, text="Class Boundaries", font=("Arial", 16),
                                               justify="center", bg="gray")
                entry_class_boundaries = Entry(top_class_bound, width=20, font=("Arial", 16), justify="center")
                entry_class_boundaries.insert(END, actual_lower_class_bound[i])
                entry_class_boundaries.insert(END, " - ")
                entry_class_boundaries.insert(END, actual_upper_class_bound[i])
                label_class_boundaries.grid(row=0, column=0)
                entry_class_boundaries.grid(row=i + 1, column=0)


        # Button for Class Boundaries Plot
        button_class_boundaries = Button(root, width=25, text="Show Class Boundaries",
                                         justify="center",
                                         command=class_bound,
                                         borderwidth=3,
                                         relief="raised")
        button_class_boundaries.grid(row=i + 2, column=0)

        # Frequency Plot
        label_frequency = Label(root, width=20, text="Frequency", font=("Arial", 16), justify="center", bg="gray")
        entry_frequency = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_frequency.insert(END, actual_frequency[i])
        label_frequency.grid(row=0, column=2)
        entry_frequency.grid(row=i + 1, column=2)
        entry_t_frequency = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_t_frequency.insert(END, "n = ")
        entry_t_frequency.insert(END, total_frequency)
        entry_t_frequency.grid(row=i + 2, column=2)

        # CM Plot
        label_cm = Label(root, width=20, text="CM", font=("Arial", 16), justify="center", bg="gray")
        entry_cm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_cm.insert(END, actual_cm[i])
        label_cm.grid(row=0, column=3)
        entry_cm.grid(row=i + 1, column=3)


        def essentials():
            top_essentials = Toplevel()
            top_essentials.title("Solutions")
            top_essentials.resizable(0, 0)
            top_essentials.geometry("400x800")

            # Scrollbar
            canva = Canvas(top_essentials)
            canva.pack(side=LEFT, fill=BOTH, expand=1)

            scroll = Scrollbar(top_essentials, orient=VERTICAL, command=canva.yview)
            scroll.pack(side=RIGHT, fill=Y)

            canva.configure(yscrollcommand=scroll.set)
            canva.bind("<Configure>", lambda e: canva.configure(scrollregion=canva.bbox("all")))

            second_framer = Frame(canva)

            canva.create_window((0, 0), window=second_framer, anchor="nw")

            # Essentials
            label_essentials = Label(second_framer, text="ESSENTIALS", font=("Arial", 16),
                                     justify="center",
                                     bg="gray",
                                     width=31)
            label_essentials.pack()

            # Lowest and Highest
            label_lowest_highest = Label(second_framer, text="Lowest and Highest", font=("Arial", 16),
                                         justify="center")
            label_lowest_highest.pack()
            text_lowest_highest = Text(second_framer, font=("Arial", 16), width=31, height=2)
            text_lowest_highest.insert(END, "Lowest = ")
            text_lowest_highest.insert(END, lowest)
            text_lowest_highest.insert(END, "\n")
            text_lowest_highest.insert(END, "Highest = ")
            text_lowest_highest.insert(END, highest)
            text_lowest_highest.pack()

            # Range
            label_range = Label(second_framer, text="Range", font=("Arial", 16),
                                justify="center")
            label_range.pack()
            text_range = Text(second_framer, font=("Arial", 16), width=31, height=3)
            text_range.insert(END, "Range = Highest - Lowest\n")
            text_range.insert(END, "Range  = {} - {}\n".format(highest, lowest))
            text_range.insert(END, "Range = {}".format(round(range_c, 2)))
            text_range.pack()

            # Number of rows
            label_num_rows = Label(second_framer, text="Number of rows", font=("Arial", 16),
                                   justify="center")
            label_num_rows.pack()
            if specify_rows.lower() == 'n':
                text_num_rows = Text(second_framer, font=("Arial", 16), width=31, height=4)
                text_num_rows.insert(END, "k = 1 + (3.3 log n)\n")
                text_num_rows.insert(END, "k = 1 + (3.3 log ({})\n".format(count_elements))
                text_num_rows.insert(END, "k = 1 + {}\n".format(3.3 * math.log10(count_elements)))
                text_num_rows.insert(END, "k = {}".format(number_rows))
            else:
                text_num_rows = Text(second_framer, font=("Arial", 16), width=31, height=1)
                text_num_rows.insert(END, "k = {}".format(number_rows))
            text_num_rows.pack()

            # class size
            label_class_size = Label(second_framer, text="Class Size (Interval)",
                                     font=("Arial", 16),
                                     justify="center")
            label_class_size.pack()
            text_class_size = Text(second_framer, font=("Arial", 16), width=31, height=3)
            text_class_size.insert(END, "c = R / k\n")
            text_class_size.insert(END, "c = {} / {}\n".format(round(range_c, 2), number_rows))
            text_class_size.insert(END, "c = {}".format(actual_class_size))
            text_class_size.pack()

            # NEEDED FOR GETTING THE MEAN, MEDIAN, MODE
            label_3m = Label(second_framer, text="FOR MEAN, MEDIAN, AND MODE",
                             font=("Arial", 16),
                             justify="center",
                             bg="gray", width=31)
            label_3m.pack()

            # Xlb
            label_xlb = Label(second_framer, text="Xlb",
                              font=("Arial", 16),
                              justify="center")
            label_xlb.pack()
            text_xlb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_xlb.insert(END, "Xlb = ")
            text_xlb.insert(END, actual_xlb)
            text_xlb.pack()

            # fb
            label_fb = Label(second_framer, text="fb",
                             font=("Arial", 16),
                             justify="center")
            label_fb.pack()
            text_fb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fb.insert(END, "fb = ")
            text_fb.insert(END, actual_fb)
            text_fb.pack()

            # fm
            label_fm = Label(second_framer, text="fm",
                             font=("Arial", 16),
                             justify="center")
            label_fm.pack()
            text_fm = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fm.insert(END, "fm = ")
            text_fm.insert(END, actual_fm)
            text_fm.pack()

            # fa
            label_fa = Label(second_framer, text="fa",
                             font=("Arial", 16),
                             justify="center")
            label_fa.pack()
            text_fa = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fa.insert(END, "fa = ")
            text_fa.insert(END, actual_fa)
            text_fa.pack()

            # cumfb
            label_cumfb = Label(second_framer, text="cumfb",
                                font=("Arial", 16),
                                justify="center")
            label_cumfb.pack()
            text_cumfb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_cumfb.insert(END, "cumfb = ")
            text_cumfb.insert(END, actual_cumfb)
            text_cumfb.pack()


        button_essentials = Button(root, text="Show Essentials",
                                   width=25,
                                   justify="center",
                                   command=essentials,
                                   borderwidth=3,
                                   relief="raised")
        button_essentials.grid(row=i + 2, column=3)

        # f(CM) Plot
        label_fcm = Label(root, width=20, text="f(CM)", font=("Arial", 16), justify="center", bg="gray")
        entry_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_fcm.insert(END, actual_fcm[i])
        label_fcm.grid(row=0, column=4)
        entry_fcm.grid(row=i + 1, column=4)
        entry_t_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_t_fcm.insert(END, "n = ")
        entry_t_fcm.insert(END, total_fcm)
        entry_t_fcm.grid(row=i + 2, column=4)

        # <cf Plot
        label_fcm = Label(root, text="<cf", font=("Arial", 16), justify="center")
        entry_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_fcm.insert(END, actual_less_cf[i])
        label_fcm.grid(row=0, column=5)
        entry_fcm.grid(row=i + 1, column=5)


        def three_m():
            top_3m = Toplevel()
            top_3m.title("Mean, Median, Mode")
            top_3m.geometry("400x370")
            top_3m.resizable(0, 0)

            # Mean
            label_mean = Label(top_3m, text="Mean", font=("Arial", 16), justify="center",
                               bg="gray", width=28)
            label_mean.pack()
            text_mean = Text(top_3m, font=("Arial", 14), width=31, height=3)
            text_mean.insert(END, "x̄ = All elements / Count of elements\n")
            text_mean.insert(END, "x̄ = {} / {}\n".format(round(sum(elements), 5), count_elements))
            text_mean.insert(END, "x̄ = {}".format(actual_mean))
            text_mean.pack()

            # Median
            label_median = Label(top_3m, text="Median", font=("Arial", 16), justify="center",
                                 bg="gray", width=28)
            label_median.pack()
            text_median = Text(top_3m, font=("Arial", 14), width=31, height=4)
            text_median.insert(END, "X ̃ = Xlb + ((n/2 - cumfb) / fm) * c\n")
            text_median.insert(END, "X ̃ = {} + (({} / 2 - {}) / {}) * {}\n".format(actual_xlb,
                                                                                    total_frequency,
                                                                                    actual_cumfb,
                                                                                    actual_fm,
                                                                                    actual_class_size))
            text_median.insert(END, "X ̃ = {} + {} * {}\n".format(actual_xlb, round(((total_frequency /
                                                                                      2 - actual_cumfb) /
                                                                                     actual_fm), 5),
                                                                  round(actual_class_size, 5)))
            text_median.insert(END, "X ̃ = {}".format(actual_median))
            text_median.pack()

            # Mode
            label_mode = Label(top_3m, text="Mode", font=("Arial", 16), justify="center",
                               bg="gray", width=28)
            label_mode.pack()
            text_mode = Text(top_3m, font=("Arial", 14), width=31, height=4)
            text_mode.insert(END, "X̂ = Xlb + (d1 / (d1 + d2)) * c\n")
            text_mode.insert(END, "X̂ = {} + ({} / ({} + {})) * {}\n".format(actual_xlb,
                                                                             actual_d1,
                                                                             actual_d1,
                                                                             actual_d2,
                                                                             round(actual_class_size, 5)))
            text_mode.insert(END, "X̂ = {} + {} * {}\n".format(actual_xlb, round((actual_d1 /
                                                                                  (actual_d1 + actual_d2)), 5),
                                                               round(actual_class_size, 5)))
            text_mode.insert(END, "X̂ = {}\n".format(actual_mode))
            text_mode.pack()


        # Button for Mean, median, mode window
        button_3m = Button(root, text="Mean, Median, Mode",
                           width=25,
                           justify="center",
                           command=three_m,
                           borderwidth=3,
                           relief="raised")
        button_3m.grid(row=i + 2, column=5)

    root.mainloop()










elif decimal_count == 1:
    while True:
        elements = list(map(float, input().split()))
        elements = sorted(elements)
        if len(elements) == count_elements:
            break

    lowest = min(elements)
    highest = max(elements)

    range_c = highest - lowest

    specify_rows = input()
    if specify_rows.lower() == 'n':
        number_rows = round(1 + (3.3 * math.log10(count_elements)))
    elif specify_rows.lower() == 'y':
        number_rows = int(input())

    specify_interval = input()
    if specify_interval.lower() == 'n':
        actual_class_size = round((range_c / number_rows), 2)
    elif specify_interval.lower() == 'y':
        actual_class_size = float(input())

    actual_lower_limit = []
    actual_upper_limit = []

    actual_limits = []

    actual_lower_class_bound = []
    actual_upper_class_bound = []

    actual_cm = []

    for i in range(number_rows):
        lower_limit = lowest + (actual_class_size * i)
        upper_limit = (lowest + (actual_class_size * (i + standard_addition_1))) - standard_addition_1
        actual_lower_limit.append(lower_limit)
        actual_upper_limit.append(upper_limit)

        limits = np.around(np.arange(actual_lower_limit[i], (actual_upper_limit[i] + standard_addition_1),
                                     standard_addition_1), 2)
        actual_limits.append(limits)

        lower_class_bound = actual_lower_limit[i] - const_1
        upper_class_bound = actual_upper_limit[i] - const_1
        actual_lower_class_bound.append(lower_class_bound)
        actual_upper_class_bound.append(upper_class_bound)

        cm = round((actual_lower_limit[i] + actual_upper_limit[i]) / 2, 2)
        actual_cm.append(cm)

    # Frequency
    freq1 = []
    freq2 = []
    freq3 = []
    freq4 = []
    freq5 = []
    freq6 = []
    freq7 = []
    freq8 = []
    freq9 = []
    freq10 = []
    freq11 = []
    freq12 = []
    freq13 = []
    freq14 = []
    freq15 = []
    freq16 = []
    freq17 = []
    freq18 = []
    freq19 = []
    freq20 = []
    freq21 = []
    freq22 = []
    freq23 = []
    freq24 = []
    freq25 = []
    freq26 = []
    freq27 = []
    freq28 = []
    freq29 = []
    freq30 = []

    try:
        for value in elements:
            if value in actual_limits[0]:
                freq1.append(value)
        for value in elements:
            if value in actual_limits[1]:
                freq2.append(value)
        for value in elements:
            if value in actual_limits[2]:
                freq3.append(value)
        for value in elements:
            if value in actual_limits[3]:
                freq4.append(value)
        for value in elements:
            if value in actual_limits[4]:
                freq5.append(value)
        for value in elements:
            if value in actual_limits[5]:
                freq6.append(value)
        for value in elements:
            if value in actual_limits[6]:
                freq7.append(value)
        for value in elements:
            if value in actual_limits[7]:
                freq8.append(value)
        for value in elements:
            if value in actual_limits[8]:
                freq9.append(value)
        for value in elements:
            if value in actual_limits[9]:
                freq10.append(value)
        for value in elements:
            if value in actual_limits[10]:
                freq11.append(value)
        for value in elements:
            if value in actual_limits[11]:
                freq12.append(value)
        for value in elements:
            if value in actual_limits[12]:
                freq13.append(value)
        for value in elements:
            if value in actual_limits[13]:
                freq14.append(value)
        for value in elements:
            if value in actual_limits[14]:
                freq15.append(value)
        for value in elements:
            if value in actual_limits[15]:
                freq16.append(value)
        for value in elements:
            if value in actual_limits[16]:
                freq17.append(value)
        for value in elements:
            if value in actual_limits[17]:
                freq18.append(value)
        for value in elements:
            if value in actual_limits[18]:
                freq19.append(value)
        for value in elements:
            if value in actual_limits[19]:
                freq20.append(value)
        for value in elements:
            if value in actual_limits[20]:
                freq21.append(value)
        for value in elements:
            if value in actual_limits[21]:
                freq22.append(value)
        for value in elements:
            if value in actual_limits[22]:
                freq23.append(value)
        for value in elements:
            if value in actual_limits[23]:
                freq24.append(value)
        for value in elements:
            if value in actual_limits[24]:
                freq25.append(value)
        for value in elements:
            if value in actual_limits[25]:
                freq26.append(value)
        for value in elements:
            if value in actual_limits[26]:
                freq27.append(value)
        for value in elements:
            if value in actual_limits[27]:
                freq28.append(value)
        for value in elements:
            if value in actual_limits[28]:
                freq29.append(value)
        for value in elements:
            if value in actual_limits[29]:
                freq30.append(value)
    except IndexError:
        pass

    len_freq1 = len(freq1)
    len_freq2 = len(freq2)
    len_freq3 = len(freq3)
    len_freq4 = len(freq4)
    len_freq5 = len(freq5)
    len_freq6 = len(freq6)
    len_freq7 = len(freq7)
    len_freq8 = len(freq8)
    len_freq9 = len(freq9)
    len_freq10 = len(freq10)
    len_freq11 = len(freq11)
    len_freq12 = len(freq12)
    len_freq13 = len(freq13)
    len_freq14 = len(freq14)
    len_freq15 = len(freq15)
    len_freq16 = len(freq16)
    len_freq17 = len(freq17)
    len_freq18 = len(freq18)
    len_freq19 = len(freq19)
    len_freq20 = len(freq20)
    len_freq21 = len(freq21)
    len_freq22 = len(freq22)
    len_freq23 = len(freq23)
    len_freq24 = len(freq24)
    len_freq25 = len(freq25)
    len_freq26 = len(freq26)
    len_freq27 = len(freq27)
    len_freq28 = len(freq28)
    len_freq29 = len(freq29)
    len_freq30 = len(freq30)

    initial_frequency = [len_freq1, len_freq2, len_freq3, len_freq4, len_freq5,
                         len_freq6, len_freq7, len_freq8, len_freq9, len_freq10,
                         len_freq11, len_freq12, len_freq13, len_freq14, len_freq15,
                         len_freq16, len_freq17, len_freq18, len_freq19, len_freq20,
                         len_freq21, len_freq22, len_freq23, len_freq24, len_freq25,
                         len_freq26, len_freq27, len_freq28, len_freq29, len_freq30]

    # frequency
    actual_frequency = [value for value in initial_frequency if value != 0]

    total_frequency = sum(actual_frequency)

    actual_fcm = []

    for i in range(number_rows):
        fcm = actual_frequency[i] * actual_cm[i]
        actual_fcm.append(fcm)

    total_fcm = sum(actual_fcm)

    actual_less_cf = []

    len_less_f = len(actual_frequency)
    for i in range(len_less_f):
        less_cf = sum(actual_frequency[:i + 1])
        actual_less_cf.append(less_cf)

    # fm, fb, fa, Xlb, and cumfb, class size

    # FM, FB, FA
    actual_fm = max(actual_frequency)  # modal class

    i_fm = actual_frequency.index(actual_fm)  # modal class

    i_fb = i_fm - 1
    i_fa = i_fm + 1

    actual_fb = actual_frequency[i_fb]

    actual_fa = actual_frequency[i_fa]

    # Xlb, cumfb
    actual_xlb = actual_lower_class_bound[i_fm]

    actual_cumfb = actual_less_cf[i_fb]

    # d1, d2
    actual_d1 = actual_fm - actual_fb
    actual_d2 = actual_fm - actual_fa

    # Mean, median, mode

    actual_mean = round(sum(elements) / count_elements, 2)

    actual_median = np.median(elements)

    actual_mode = round(actual_xlb + (actual_d1 / (actual_d1 + actual_d2) * actual_class_size), 2)

    # GUI Tkinter

    root = Tk()
    root.title("Frequency Distribution Table")
    root.resizable(0, 0)

    for i in range(number_rows):
        # Class Interval Plot
        label_class_interval = Label(root, width=20, text="Scores (Class Interval)", font=("Arial", 16), justify="center",
                                     bg="gray")
        entry_class_interval = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_class_interval.insert(END, actual_lower_limit[i])
        entry_class_interval.insert(END, " - ")
        entry_class_interval.insert(END, actual_upper_limit[i])
        label_class_interval.grid(row=0, column=0)
        entry_class_interval.grid(row=i + 1, column=0)


        def class_bound():
            top_class_bound = Toplevel()
            top_class_bound.resizable(0, 0)
            # Class Boundaries Plot
            for i in range(number_rows):
                label_class_boundaries = Label(top_class_bound, width=20, text="Class Boundaries", font=("Arial", 16),
                                               justify="center", bg="gray")
                entry_class_boundaries = Entry(top_class_bound, width=20, font=("Arial", 16), justify="center")
                entry_class_boundaries.insert(END, actual_lower_class_bound[i])
                entry_class_boundaries.insert(END, " - ")
                entry_class_boundaries.insert(END, actual_upper_class_bound[i])
                label_class_boundaries.grid(row=0, column=0)
                entry_class_boundaries.grid(row=i + 1, column=0)


        # Button for Class Boundaries Plot
        button_class_boundaries = Button(root, width=25, text="Show Class Boundaries",
                                         justify="center",
                                         command=class_bound,
                                         borderwidth=3,
                                         relief="raised")
        button_class_boundaries.grid(row=i + 2, column=0)

        # Frequency Plot
        label_frequency = Label(root, width=20, text="Frequency", font=("Arial", 16), justify="center", bg="gray")
        entry_frequency = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_frequency.insert(END, actual_frequency[i])
        label_frequency.grid(row=0, column=2)
        entry_frequency.grid(row=i + 1, column=2)
        entry_t_frequency = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_t_frequency.insert(END, "n = ")
        entry_t_frequency.insert(END, total_frequency)
        entry_t_frequency.grid(row=i + 2, column=2)

        # CM Plot
        label_cm = Label(root, width=20, text="CM", font=("Arial", 16), justify="center", bg="gray")
        entry_cm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_cm.insert(END, actual_cm[i])
        label_cm.grid(row=0, column=3)
        entry_cm.grid(row=i + 1, column=3)


        def essentials():
            top_essentials = Toplevel()
            top_essentials.title("Solutions")
            top_essentials.resizable(0, 0)
            top_essentials.geometry("400x800")

            # Scrollbar
            canva = Canvas(top_essentials)
            canva.pack(side=LEFT, fill=BOTH, expand=1)

            scroll = Scrollbar(top_essentials, orient=VERTICAL, command=canva.yview)
            scroll.pack(side=RIGHT, fill=Y)

            canva.configure(yscrollcommand=scroll.set)
            canva.bind("<Configure>", lambda e: canva.configure(scrollregion=canva.bbox("all")))

            second_framer = Frame(canva)

            canva.create_window((0, 0), window=second_framer, anchor="nw")

            # Essentials
            label_essentials = Label(second_framer, text="ESSENTIALS", font=("Arial", 16),
                                     justify="center",
                                     bg="gray",
                                     width=31)
            label_essentials.pack()

            # Lowest and Highest
            label_lowest_highest = Label(second_framer, text="Lowest and Highest", font=("Arial", 16),
                                         justify="center")
            label_lowest_highest.pack()
            text_lowest_highest = Text(second_framer, font=("Arial", 16), width=31, height=2)
            text_lowest_highest.insert(END, "Lowest = ")
            text_lowest_highest.insert(END, lowest)
            text_lowest_highest.insert(END, "\n")
            text_lowest_highest.insert(END, "Highest = ")
            text_lowest_highest.insert(END, highest)
            text_lowest_highest.pack()

            # Range
            label_range = Label(second_framer, text="Range", font=("Arial", 16),
                                justify="center")
            label_range.pack()
            text_range = Text(second_framer, font=("Arial", 16), width=31, height=3)
            text_range.insert(END, "Range = Highest - Lowest\n")
            text_range.insert(END, "Range  = {} - {}\n".format(highest, lowest))
            text_range.insert(END, "Range = {}".format(round(range_c, 2)))
            text_range.pack()

            # Number of rows
            label_num_rows = Label(second_framer, text="Number of rows", font=("Arial", 16),
                                   justify="center")
            label_num_rows.pack()
            if specify_rows.lower() == 'n':
                text_num_rows = Text(second_framer, font=("Arial", 16), width=31, height=4)
                text_num_rows.insert(END, "k = 1 + (3.3 log n)\n")
                text_num_rows.insert(END, "k = 1 + (3.3 log ({})\n".format(count_elements))
                text_num_rows.insert(END, "k = 1 + {}\n".format(3.3 * math.log10(count_elements)))
                text_num_rows.insert(END, "k = {}".format(number_rows))
            else:
                text_num_rows = Text(second_framer, font=("Arial", 16), width=31, height=1)
                text_num_rows.insert(END, "k = {}".format(number_rows))
            text_num_rows.pack()

            # class size
            label_class_size = Label(second_framer, text="Class Size (Interval)",
                                     font=("Arial", 16),
                                     justify="center")
            label_class_size.pack()
            text_class_size = Text(second_framer, font=("Arial", 16), width=31, height=3)
            text_class_size.insert(END, "c = R / k\n")
            text_class_size.insert(END, "c = {} / {}\n".format(round(range_c, 2), number_rows))
            text_class_size.insert(END, "c = {}".format(actual_class_size))
            text_class_size.pack()

            # NEEDED FOR GETTING THE MEAN, MEDIAN, MODE
            label_3m = Label(second_framer, text="FOR MEAN, MEDIAN, AND MODE",
                             font=("Arial", 16),
                             justify="center",
                             bg="gray", width=31)
            label_3m.pack()

            # Xlb
            label_xlb = Label(second_framer, text="Xlb",
                              font=("Arial", 16),
                              justify="center")
            label_xlb.pack()
            text_xlb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_xlb.insert(END, "Xlb = ")
            text_xlb.insert(END, actual_xlb)
            text_xlb.pack()

            # fb
            label_fb = Label(second_framer, text="fb",
                             font=("Arial", 16),
                             justify="center")
            label_fb.pack()
            text_fb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fb.insert(END, "fb = ")
            text_fb.insert(END, actual_fb)
            text_fb.pack()

            # fm
            label_fm = Label(second_framer, text="fm",
                             font=("Arial", 16),
                             justify="center")
            label_fm.pack()
            text_fm = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fm.insert(END, "fm = ")
            text_fm.insert(END, actual_fm)
            text_fm.pack()

            # fa
            label_fa = Label(second_framer, text="fa",
                             font=("Arial", 16),
                             justify="center")
            label_fa.pack()
            text_fa = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fa.insert(END, "fa = ")
            text_fa.insert(END, actual_fa)
            text_fa.pack()

            # cumfb
            label_cumfb = Label(second_framer, text="cumfb",
                                font=("Arial", 16),
                                justify="center")
            label_cumfb.pack()
            text_cumfb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_cumfb.insert(END, "cumfb = ")
            text_cumfb.insert(END, actual_cumfb)
            text_cumfb.pack()


        button_essentials = Button(root, text="Show Essentials",
                                   width=25,
                                   justify="center",
                                   command=essentials,
                                   borderwidth=3,
                                   relief="raised")
        button_essentials.grid(row=i + 2, column=3)

        # f(CM) Plot
        label_fcm = Label(root, width=20, text="f(CM)", font=("Arial", 16), justify="center", bg="gray")
        entry_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_fcm.insert(END, actual_fcm[i])
        label_fcm.grid(row=0, column=4)
        entry_fcm.grid(row=i + 1, column=4)
        entry_t_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_t_fcm.insert(END, "n = ")
        entry_t_fcm.insert(END, total_fcm)
        entry_t_fcm.grid(row=i + 2, column=4)

        # <cf Plot
        label_fcm = Label(root, width=20, text="<cf", font=("Arial", 16), justify="center", bg="gray")
        entry_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_fcm.insert(END, actual_less_cf[i])
        label_fcm.grid(row=0, column=5)
        entry_fcm.grid(row=i + 1, column=5)


        def three_m():
            top_3m = Toplevel()
            top_3m.title("Mean, Median, Mode")
            top_3m.geometry("400x370")
            top_3m.resizable(0, 0)

            # Mean
            label_mean = Label(top_3m, text="Mean", font=("Arial", 16), justify="center",
                               bg="gray", width=28)
            label_mean.pack()
            text_mean = Text(top_3m, font=("Arial", 14), width=31, height=3)
            text_mean.insert(END, "x̄ = All elements / Count of elements\n")
            text_mean.insert(END, "x̄ = {} / {}\n".format(round(sum(elements), 5), count_elements))
            text_mean.insert(END, "x̄ = {}".format(actual_mean))
            text_mean.pack()

            # Median
            label_median = Label(top_3m, text="Median", font=("Arial", 16), justify="center",
                                 bg="gray", width=28)
            label_median.pack()
            text_median = Text(top_3m, font=("Arial", 14), width=31, height=4)
            text_median.insert(END, "X ̃ = Xlb + ((n/2 - cumfb) / fm) * c\n")
            text_median.insert(END, "X ̃ = {} + (({} / 2 - {}) / {}) * {}\n".format(actual_xlb,
                                                                                    total_frequency,
                                                                                    actual_cumfb,
                                                                                    actual_fm,
                                                                                    actual_class_size))
            text_median.insert(END, "X ̃ = {} + {} * {}\n".format(actual_xlb, round(((total_frequency /
                                                                                      2 - actual_cumfb) /
                                                                                     actual_fm), 5),
                                                                  round(actual_class_size, 5)))
            text_median.insert(END, "X ̃ = {}".format(actual_median))
            text_median.pack()

            # Mode
            label_mode = Label(top_3m, text="Mode", font=("Arial", 16), justify="center",
                               bg="gray", width=28)
            label_mode.pack()
            text_mode = Text(top_3m, font=("Arial", 14), width=31, height=4)
            text_mode.insert(END, "X̂ = Xlb + (d1 / (d1 + d2)) * c\n")
            text_mode.insert(END, "X̂ = {} + ({} / ({} + {})) * {}\n".format(actual_xlb,
                                                                             actual_d1,
                                                                             actual_d1,
                                                                             actual_d2,
                                                                             round(actual_class_size, 5)))
            text_mode.insert(END, "X̂ = {} + {} * {}\n".format(actual_xlb, round((actual_d1 /
                                                                                  (actual_d1 + actual_d2)), 5),
                                                               round(actual_class_size, 5)))
            text_mode.insert(END, "X̂ = {}\n".format(actual_mode))
            text_mode.pack()


        # Button for Mean, median, mode window
        button_3m = Button(root, text="Mean, Median, Mode",
                           width=25,
                           justify="center",
                           command=three_m,
                           borderwidth=3,
                           relief="raised")
        button_3m.grid(row=i + 2, column=5)

    root.mainloop()










elif decimal_count == 2:
    while True:
        elements = list(map(float, input().split()))  # values # float or int
        elements = sorted(elements)
        if len(elements) == count_elements:
            break

    # STARTING OBTAINING VALUES

    lowest = min(elements)
    highest = max(elements)

    range_c = highest - lowest

    # number of rows
    specify_rows = input()  # yes or no
    if specify_rows.lower() == 'n':
        number_rows = round(1 + (3.3 * math.log10(count_elements)))
    elif specify_rows.lower() == 'y':
        number_rows = int(input())  # input specified rows

    # class size (interval)
    specify_interval = input()  # yes or no
    if specify_interval.lower() == 'n':
        actual_class_size = round((range_c / number_rows), 2)
    if specify_interval.lower() == 'y':
        actual_class_size = float(input())  # input specified interval

    # STARTING POINT

    # lower limits and upper limits (Class Interval)
    actual_lower_limit = []
    actual_upper_limit = []

    # Class boundaries
    actual_lower_class_bound = []
    actual_upper_class_bound = []

    # limits within class size
    actual_limits = []

    # CM
    actual_cm = []

    for i in range(number_rows):
        lower_l = lowest + (actual_class_size * i)
        upper_l = (lowest + (actual_class_size * (i + 1))) - standard_addition_2
        r2_lower_l = round(lower_l, 2)
        r2_upper_l = round(upper_l, 2)
        actual_lower_limit.append(r2_lower_l)
        actual_upper_limit.append(r2_upper_l)

        class_bound_lower = round(actual_lower_limit[i] - const_2, 3)
        class_bound_upper = round(actual_upper_limit[i] - const_2, 3)
        actual_lower_class_bound.append(class_bound_lower)
        actual_upper_class_bound.append(class_bound_upper)

        limits = np.around(np.arange(actual_lower_limit[i], (actual_upper_limit[i] + standard_addition_2),
                                     standard_addition_2), 2)
        actual_limits.append(limits)

        cm = round((r2_lower_l + r2_upper_l) / 2, 2)
        actual_cm.append(cm)

    freq1 = []
    freq2 = []
    freq3 = []
    freq4 = []
    freq5 = []
    freq6 = []
    freq7 = []
    freq8 = []
    freq9 = []
    freq10 = []
    freq11 = []
    freq12 = []
    freq13 = []
    freq14 = []
    freq15 = []
    freq16 = []
    freq17 = []
    freq18 = []
    freq19 = []
    freq20 = []
    freq21 = []
    freq22 = []
    freq23 = []
    freq24 = []
    freq25 = []
    freq26 = []
    freq27 = []
    freq28 = []
    freq29 = []
    freq30 = []

    try:
        for value in elements:
            if value in actual_limits[0]:
                freq1.append(value)
        for value in elements:
            if value in actual_limits[1]:
                freq2.append(value)
        for value in elements:
            if value in actual_limits[2]:
                freq3.append(value)
        for value in elements:
            if value in actual_limits[3]:
                freq4.append(value)
        for value in elements:
            if value in actual_limits[4]:
                freq5.append(value)
        for value in elements:
            if value in actual_limits[5]:
                freq6.append(value)
        for value in elements:
            if value in actual_limits[6]:
                freq7.append(value)
        for value in elements:
            if value in actual_limits[7]:
                freq8.append(value)
        for value in elements:
            if value in actual_limits[8]:
                freq9.append(value)
        for value in elements:
            if value in actual_limits[9]:
                freq10.append(value)
        for value in elements:
            if value in actual_limits[10]:
                freq11.append(value)
        for value in elements:
            if value in actual_limits[11]:
                freq12.append(value)
        for value in elements:
            if value in actual_limits[12]:
                freq13.append(value)
        for value in elements:
            if value in actual_limits[13]:
                freq14.append(value)
        for value in elements:
            if value in actual_limits[14]:
                freq15.append(value)
        for value in elements:
            if value in actual_limits[15]:
                freq16.append(value)
        for value in elements:
            if value in actual_limits[16]:
                freq17.append(value)
        for value in elements:
            if value in actual_limits[17]:
                freq18.append(value)
        for value in elements:
            if value in actual_limits[18]:
                freq19.append(value)
        for value in elements:
            if value in actual_limits[19]:
                freq20.append(value)
        for value in elements:
            if value in actual_limits[20]:
                freq21.append(value)
        for value in elements:
            if value in actual_limits[21]:
                freq22.append(value)
        for value in elements:
            if value in actual_limits[22]:
                freq23.append(value)
        for value in elements:
            if value in actual_limits[23]:
                freq24.append(value)
        for value in elements:
            if value in actual_limits[24]:
                freq25.append(value)
        for value in elements:
            if value in actual_limits[25]:
                freq26.append(value)
        for value in elements:
            if value in actual_limits[26]:
                freq27.append(value)
        for value in elements:
            if value in actual_limits[27]:
                freq28.append(value)
        for value in elements:
            if value in actual_limits[28]:
                freq29.append(value)
        for value in elements:
            if value in actual_limits[29]:
                freq30.append(value)
    except IndexError:
        pass

    len_freq1 = len(freq1)
    len_freq2 = len(freq2)
    len_freq3 = len(freq3)
    len_freq4 = len(freq4)
    len_freq5 = len(freq5)
    len_freq6 = len(freq6)
    len_freq7 = len(freq7)
    len_freq8 = len(freq8)
    len_freq9 = len(freq9)
    len_freq10 = len(freq10)
    len_freq11 = len(freq11)
    len_freq12 = len(freq12)
    len_freq13 = len(freq13)
    len_freq14 = len(freq14)
    len_freq15 = len(freq15)
    len_freq16 = len(freq16)
    len_freq17 = len(freq17)
    len_freq18 = len(freq18)
    len_freq19 = len(freq19)
    len_freq20 = len(freq20)
    len_freq21 = len(freq21)
    len_freq22 = len(freq22)
    len_freq23 = len(freq23)
    len_freq24 = len(freq24)
    len_freq25 = len(freq25)
    len_freq26 = len(freq26)
    len_freq27 = len(freq27)
    len_freq28 = len(freq28)
    len_freq29 = len(freq29)
    len_freq30 = len(freq30)

    initial_frequency = [len_freq1, len_freq2, len_freq3, len_freq4, len_freq5,
                         len_freq6, len_freq7, len_freq8, len_freq9, len_freq10,
                         len_freq11, len_freq12, len_freq13, len_freq14, len_freq15,
                         len_freq16, len_freq17, len_freq18, len_freq19, len_freq20,
                         len_freq21, len_freq22, len_freq23, len_freq24, len_freq25,
                         len_freq26, len_freq27, len_freq28, len_freq29, len_freq30]

    # frequency
    actual_frequency = [value for value in initial_frequency if value != 0]

    # total frequecy
    total_frequency = sum(actual_frequency)

    # actual f(CM)
    actual_fcm = []

    for i in range(number_rows):
        fcm = actual_frequency[i] * actual_cm[i]
        r2_fcm = round(fcm, 2)
        actual_fcm.append(r2_fcm)

    # total f(CM)
    total_fcm = sum(actual_fcm)

    # <cf
    actual_less_cf = []

    len_less_f = len(actual_frequency)
    for i in range(len_less_f):
        less_cf = sum(actual_frequency[:i + 1])
        actual_less_cf.append(less_cf)

    # fm, fb, fa, Xlb, and cumfb, class size

    # FM, FB, FA
    actual_fm = max(actual_frequency)  # modal class

    i_fm = actual_frequency.index(actual_fm)  # modal class

    i_fb = i_fm - 1
    i_fa = i_fm + 1

    actual_fb = actual_frequency[i_fb]

    actual_fa = actual_frequency[i_fa]

    # Xlb, cumfb
    actual_xlb = actual_lower_class_bound[i_fm]

    actual_cumfb = actual_less_cf[i_fb]

    # d1, d2
    actual_d1 = actual_fm - actual_fb
    actual_d2 = actual_fm - actual_fa

    # Mean, median, mode

    actual_mean = round(sum(elements) / count_elements, 2)

    actual_median = np.median(elements)

    actual_mode = round(actual_xlb + (actual_d1 / (actual_d1 + actual_d2) * actual_class_size), 2)

    # GUI Tkinter

    root = Tk()
    root.title("Frequency Distribution Table")
    root.resizable(0, 0)

    for i in range(number_rows):
        # Class Interval Plot
        label_class_interval = Label(root, width=20, text="Scores (Class Interval)", font=("Arial", 16), justify="center",
                                     bg="gray")
        entry_class_interval = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_class_interval.insert(END, actual_lower_limit[i])
        entry_class_interval.insert(END, " - ")
        entry_class_interval.insert(END, actual_upper_limit[i])
        label_class_interval.grid(row=0, column=0)
        entry_class_interval.grid(row=i + 1, column=0)


        def class_bound():
            top_class_bound = Toplevel()
            top_class_bound.resizable(0, 0)
            # Class Boundaries Plot
            for i in range(number_rows):
                label_class_boundaries = Label(top_class_bound, width=20, text="Class Boundaries", font=("Arial", 16),
                                               justify="center",
                                               bg="gray")
                entry_class_boundaries = Entry(top_class_bound, width=20, font=("Arial", 16), justify="center")
                entry_class_boundaries.insert(END, actual_lower_class_bound[i])
                entry_class_boundaries.insert(END, " - ")
                entry_class_boundaries.insert(END, actual_upper_class_bound[i])
                label_class_boundaries.grid(row=0, column=0)
                entry_class_boundaries.grid(row=i + 1, column=0)


        # Button for Class Boundaries Plot
        button_class_boundaries = Button(root, width=25, text="Show Class Boundaries",
                                         justify="center",
                                         command=class_bound,
                                         borderwidth=3,
                                         relief="raised")
        button_class_boundaries.grid(row=i + 2, column=0)

        # Frequency Plot
        label_frequency = Label(root, width=20, text="Frequency", font=("Arial", 16), justify="center",
                                bg="gray")
        entry_frequency = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_frequency.insert(END, actual_frequency[i])
        label_frequency.grid(row=0, column=2)
        entry_frequency.grid(row=i + 1, column=2)
        entry_t_frequency = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_t_frequency.insert(END, "n = ")
        entry_t_frequency.insert(END, total_frequency)
        entry_t_frequency.grid(row=i + 2, column=2)

        # CM Plot
        label_cm = Label(root, width=20, text="CM", font=("Arial", 16), justify="center", bg="gray")
        entry_cm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_cm.insert(END, actual_cm[i])
        label_cm.grid(row=0, column=3)
        entry_cm.grid(row=i + 1, column=3)


        def essentials():
            top_essentials = Toplevel()
            top_essentials.title("Solutions")
            top_essentials.resizable(0, 0)
            top_essentials.geometry("400x800")

            # Scrollbar
            canva = Canvas(top_essentials)
            canva.pack(side=LEFT, fill=BOTH, expand=1)

            scroll = Scrollbar(top_essentials, orient=VERTICAL, command=canva.yview)
            scroll.pack(side=RIGHT, fill=Y)

            canva.configure(yscrollcommand=scroll.set)
            canva.bind("<Configure>", lambda e: canva.configure(scrollregion=canva.bbox("all")))

            second_framer = Frame(canva)

            canva.create_window((0, 0), window=second_framer, anchor="nw")

            # Essentials
            label_essentials = Label(second_framer, text="ESSENTIALS", font=("Arial", 16),
                                     justify="center",
                                     bg="gray",
                                     width=31)
            label_essentials.pack()

            # Lowest and Highest
            label_lowest_highest = Label(second_framer, text="Lowest and Highest", font=("Arial", 16),
                                         justify="center")
            label_lowest_highest.pack()
            text_lowest_highest = Text(second_framer, font=("Arial", 16), width=31, height=2)
            text_lowest_highest.insert(END, "Lowest = ")
            text_lowest_highest.insert(END, lowest)
            text_lowest_highest.insert(END, "\n")
            text_lowest_highest.insert(END, "Highest = ")
            text_lowest_highest.insert(END, highest)
            text_lowest_highest.pack()

            # Range
            label_range = Label(second_framer, text="Range", font=("Arial", 16),
                                justify="center")
            label_range.pack()
            text_range = Text(second_framer, font=("Arial", 16), width=31, height=3)
            text_range.insert(END, "Range = Highest - Lowest\n")
            text_range.insert(END, "Range  = {} - {}\n".format(highest, lowest))
            text_range.insert(END, "Range = {}".format(round(range_c, 2)))
            text_range.pack()

            # Number of rows
            label_num_rows = Label(second_framer, text="Number of rows", font=("Arial", 16),
                                   justify="center")
            label_num_rows.pack()
            if specify_rows.lower() == 'n':
                text_num_rows = Text(second_framer, font=("Arial", 16), width=31, height=4)
                text_num_rows.insert(END, "k = 1 + (3.3 log n)\n")
                text_num_rows.insert(END, "k = 1 + (3.3 log ({})\n".format(count_elements))
                text_num_rows.insert(END, "k = 1 + {}\n".format(3.3 * math.log10(count_elements)))
                text_num_rows.insert(END, "k = {}".format(number_rows))
            else:
                text_num_rows = Text(second_framer, font=("Arial", 16), width=31, height=1)
                text_num_rows.insert(END, "k = {}".format(number_rows))
            text_num_rows.pack()

            # class size
            label_class_size = Label(second_framer, text="Class Size (Interval)",
                                     font=("Arial", 16),
                                     justify="center")
            label_class_size.pack()
            text_class_size = Text(second_framer, font=("Arial", 16), width=31, height=3)
            text_class_size.insert(END, "c = R / k\n")
            text_class_size.insert(END, "c = {} / {}\n".format(round(range_c, 2), number_rows))
            text_class_size.insert(END, "c = {}".format(actual_class_size))
            text_class_size.pack()

            # NEEDED FOR GETTING THE MEAN, MEDIAN, MODE
            label_3m = Label(second_framer, text="FOR MEAN, MEDIAN, AND MODE",
                             font=("Arial", 16),
                             justify="center",
                             bg="gray", width=31)
            label_3m.pack()

            # Xlb
            label_xlb = Label(second_framer, text="Xlb",
                              font=("Arial", 16),
                              justify="center")
            label_xlb.pack()
            text_xlb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_xlb.insert(END, "Xlb = ")
            text_xlb.insert(END, actual_xlb)
            text_xlb.pack()

            # fb
            label_fb = Label(second_framer, text="fb",
                             font=("Arial", 16),
                             justify="center")
            label_fb.pack()
            text_fb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fb.insert(END, "fb = ")
            text_fb.insert(END, actual_fb)
            text_fb.pack()

            # fm
            label_fm = Label(second_framer, text="fm",
                             font=("Arial", 16),
                             justify="center")
            label_fm.pack()
            text_fm = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fm.insert(END, "fm = ")
            text_fm.insert(END, actual_fm)
            text_fm.pack()

            # fa
            label_fa = Label(second_framer, text="fa",
                             font=("Arial", 16),
                             justify="center")
            label_fa.pack()
            text_fa = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_fa.insert(END, "fa = ")
            text_fa.insert(END, actual_fa)
            text_fa.pack()

            # cumfb
            label_cumfb = Label(second_framer, text="cumfb",
                                font=("Arial", 16),
                                justify="center")
            label_cumfb.pack()
            text_cumfb = Text(second_framer, font=("Arial", 16), width=31, height=1)
            text_cumfb.insert(END, "cumfb = ")
            text_cumfb.insert(END, actual_cumfb)
            text_cumfb.pack()


        button_essentials = Button(root, text="Show Essentials",
                                   width=25,
                                   justify="center",
                                   command=essentials,
                                   borderwidth=3,
                                   relief="raised")
        button_essentials.grid(row=i + 2, column=3)

        # f(CM) Plot
        label_fcm = Label(root, width=20, text="f(CM)", font=("Arial", 16), justify="center", bg="gray")
        entry_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_fcm.insert(END, actual_fcm[i])
        label_fcm.grid(row=0, column=4)
        entry_fcm.grid(row=i + 1, column=4)
        entry_t_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_t_fcm.insert(END, "n = ")
        entry_t_fcm.insert(END, total_fcm)
        entry_t_fcm.grid(row=i + 2, column=4)

        # <cf Plot
        label_fcm = Label(root, width=20, text="<cf", font=("Arial", 16), justify="center", bg="gray")
        entry_fcm = Entry(root, width=20, font=("Arial", 16), justify="center")
        entry_fcm.insert(END, actual_less_cf[i])
        label_fcm.grid(row=0, column=5)
        entry_fcm.grid(row=i + 1, column=5)


        def three_m():
            top_3m = Toplevel()
            top_3m.title("Mean, Median, Mode")
            top_3m.geometry("400x370")
            top_3m.resizable(0, 0)

            # Mean
            label_mean = Label(top_3m, text="Mean", font=("Arial", 16), justify="center",
                               bg="gray", width=28)
            label_mean.pack()
            text_mean = Text(top_3m, font=("Arial", 14), width=31, height=3)
            text_mean.insert(END, "x̄ = All elements / Count of elements\n")
            text_mean.insert(END, "x̄ = {} / {}\n".format(round(sum(elements), 5), count_elements))
            text_mean.insert(END, "x̄ = {}".format(actual_mean))
            text_mean.pack()

            # Median
            label_median = Label(top_3m, text="Median", font=("Arial", 16), justify="center",
                                 bg="gray", width=28)
            label_median.pack()
            text_median = Text(top_3m, font=("Arial", 14), width=31, height=4)
            text_median.insert(END, "X ̃ = Xlb + ((n/2 - cumfb) / fm) * c\n")
            text_median.insert(END, "X ̃ = {} + (({} / 2 - {}) / {}) * {}\n".format(actual_xlb,
                                                                                    total_frequency,
                                                                                    actual_cumfb,
                                                                                    actual_fm,
                                                                                    actual_class_size))
            text_median.insert(END, "X ̃ = {} + {} * {}\n".format(actual_xlb, round(((total_frequency /
                                                                                      2 - actual_cumfb) /
                                                                                     actual_fm), 5),
                                                                  round(actual_class_size, 5)))
            text_median.insert(END, "X ̃ = {}".format(actual_median))
            text_median.pack()

            # Mode
            label_mode = Label(top_3m, text="Mode", font=("Arial", 16), justify="center",
                               bg="gray", width=28)
            label_mode.pack()
            text_mode = Text(top_3m, font=("Arial", 14), width=31, height=4)
            text_mode.insert(END, "X̂ = Xlb + (d1 / (d1 + d2)) * c\n")
            text_mode.insert(END, "X̂ = {} + ({} / ({} + {})) * {}\n".format(actual_xlb,
                                                                             actual_d1,
                                                                             actual_d1,
                                                                             actual_d2,
                                                                             round(actual_class_size, 5)))
            text_mode.insert(END, "X̂ = {} + {} * {}\n".format(actual_xlb, round((actual_d1 /
                                                                                  (actual_d1 + actual_d2)), 5),
                                                               round(actual_class_size, 5)))
            text_mode.insert(END, "X̂ = {}\n".format(actual_mode))
            text_mode.pack()


        # Button for Mean, median, mode window
        button_3m = Button(root, text="Mean, Median, Mode",
                           width=25,
                           justify="center",
                           command=three_m,
                           borderwidth=3,
                           relief="raised")
        button_3m.grid(row=i + 2, column=5)

    root.mainloop()
    
