add_executable(pio_ws2812)

# generate the header file into the source tree as it is included in the RP2040 datasheet
pico_generate_pio_header(pio_ws2812 ${CMAKE_CURRENT_LIST_DIR}/uart_tx.pio OUTPUT_DIR ${CMAKE_CURRENT_LIST_DIR}/generated)
pico_generate_pio_header(pio_ws2812 ${CMAKE_CURRENT_LIST_DIR}/uart_rx.pio OUTPUT_DIR ${CMAKE_CURRENT_LIST_DIR}/generated)

target_sources(pio_ws2812 PRIVATE 
	rxtx.c 
	uart_rx.pio.h 
	uart_tx.pio.h
	LCD_st7735.c 
	LCD_st7735.h 
	DEV_Config.c 
	DEV_Config.h
	fonts.c
	fonts.h
	)

# enable usb output, disable uart output
pico_enable_stdio_usb(pio_ws2812 1)
pico_enable_stdio_uart(pio_ws2812 1)

target_link_libraries(pio_ws2812 PRIVATE 
	pico_stdlib 
	hardware_pio   
	hardware_dma 
	hardware_i2c
	hardware_uart
	pico_multicore
	hardware_clocks
	hardware_pwm
	hardware_spi
	)

pico_add_extra_outputs(pio_ws2812)

# add url via pico_set_program_url
example_auto_set_url(pio_ws2812)

