iostat-cli --data stats/iostat_1.output --disk sda3 --fig-output plots/iostat_1.png  plot --title "Random Read Size 200MB"
iostat-cli --data stats/iostat_2.output --disk sda3 --fig-output plots/iostat_2.png  plot --title "Random Write Size 200MB"
iostat-cli --data stats/iostat_3.output --disk sda3 --fig-output plots/iostat_3.png  plot --title "Sequential Read Size 200MB"
iostat-cli --data stats/iostat_4.output --disk sda3 --fig-output plots/iostat_4.png  plot --title "Sequential Write Size 200MB"
iostat-cli --data stats/iostat_5.output --disk sda3 --fig-output plots/iostat_5.png  plot --title "Random Read with Variable Size (max 500MB)"
iostat-cli --data stats/iostat_6.output --disk sda3 --fig-output plots/iostat_6.png  plot --title "Random Write with Variable Size (max 500MB)"
iostat-cli --data stats/iostat_all.output --disk sda3 --fig-output plots/iostat_all.png  plot --title "All plots in one"