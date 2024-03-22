**12 Hertz video analysis**

Do you want to see how many videos contain an underlying 12Hz frequency? Here is one way to do that.

**Instructions**

You can either download the code and run the python file extract_hertz_local.py (after installing the requirements), or run it online for < 10mb videos by adding a Github Issue and uploading the video. The video will then be processed, and the results stored, in a Github Action (see Actions page). Here's a gif showing how that works:
![hertz](https://github.com/reecpj/hertz-extractor/assets/54263157/da2b0704-7831-417b-a4e9-fda49597e61e)

I show a previous video's results in the above screen recording so you don't have to wait for the action to finish.

You'll need a Github account to add Issues, and they're public.

**Results**
I write out the average amplitude for a variety of audio frequencies including 12 Hz, both across the whole audio track, and across 10s chunks. All amplitudes are negative, and those closest to 0 are very high.
The last 10s chunk is less reliable than the others, as it may be less than 10s.
The 2 videos I have tested have the following results. 

```
*Coca cola ad*

mean magnitude at 10hz: -47.31
mean magnitude at 10hz for every 10s chunk: ['-52.63', '-37.42', '-48.30', '-80.00']
mean magnitude at 12hz: -45.65
mean magnitude at 12hz for every 10s chunk: ['-48.47', '-34.77', '-49.96', '-80.00']
mean magnitude at 14hz: -45.65
mean magnitude at 14hz for every 10s chunk: ['-48.47', '-34.77', '-49.96', '-80.00']
mean magnitude at 20hz: -45.65
mean magnitude at 20hz for every 10s chunk: ['-48.47', '-34.77', '-49.96', '-80.00']
mean magnitude at 60hz: -31.27
mean magnitude at 60hz for every 10s chunk: ['-26.05', '-21.17', '-41.27', '-80.00']
mean magnitude at 100hz: -29.04
mean magnitude at 100hz for every 10s chunk: ['-25.20', '-20.99', '-35.37', '-80.00']
mean magnitude at 400hz: -28.34
mean magnitude at 400hz for every 10s chunk: ['-26.95', '-19.96', '-32.48', '-80.00']


*12 Hz Strong Frequency for Focus*

mean magnitude at 10hz: -24.28
mean magnitude at 10hz for every 10s chunk: ['-28.15', '-23.82', '-23.69', '-23.62', '-23.78', '-23.75', '-23.75', '-23.70', '-23.72', '-23.82', '-23.77', '-23.71', '-23.77', '-36.34']
mean magnitude at 12hz: -3.61
mean magnitude at 12hz for every 10s chunk: ['-8.07', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-16.02']
mean magnitude at 14hz: -3.61
mean magnitude at 14hz for every 10s chunk: ['-8.07', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-16.02']
mean magnitude at 20hz: -3.61
mean magnitude at 20hz for every 10s chunk: ['-8.07', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-3.02', '-16.02']
mean magnitude at 60hz: -10.27
mean magnitude at 60hz for every 10s chunk: ['-14.53', '-9.71', '-9.70', '-9.70', '-9.71', '-9.71', '-9.71', '-9.71', '-9.71', '-9.70', '-9.71', '-9.70', '-9.71', '-22.52']
mean magnitude at 100hz: -42.16
mean magnitude at 100hz for every 10s chunk: ['-45.14', '-41.78', '-41.60', '-41.55', '-41.70', '-41.60', '-41.80', '-41.83', '-41.72', '-41.74', '-41.85', '-41.56', '-41.80', '-53.49']
mean magnitude at 400hz: -53.94
mean magnitude at 400hz for every 10s chunk: ['-54.31', '-53.90', '-54.14', '-53.72', '-53.37', '-54.09', '-53.73', '-53.38', '-53.87', '-53.50', '-53.81', '-53.90', '-53.40', '-63.96']```
