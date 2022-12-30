/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "uart_tx.pio.h"
#include <stdio.h>
#include "uart_rx.pio.h"
#include "hardware/clocks.h"
#include "LCD_st7735.h"

// normally attachc UART0 to.
// const uint PIN_TX = 0;
// This is the same as the default UART baud rate on Pico
// const uint SERIAL_BAUD = 115200;
const uint SERIAL_BAUD = 115200;
// normally attach UART1 to.
// const uint PIN_RX = 1;
#define PIN_TX 0
#define PIN_RX 1

void game_init(){
     ST7735_FillScreen(ST7735_BLACK);
     while (true){
        char c = uart_rx_program_getc(pio1,0);
        putchar(c);
        if (c == '1'){
            ST7735_WriteString(7, 20, "LAUNCH", Font_11x18, ST7735_BLACK, ST7735_CYAN);
        }
        else if (c == '2'){
            ST7735_WriteString(23, 45, "PAD", Font_11x18, ST7735_BLACK, ST7735_GREEN);
        }
        else if (c == '3'){
            ST7735_WriteString(12, 70, "MUSIC", Font_11x18, ST7735_BLACK, ST7735_YELLOW);
        }
        else if (c == '4'){
            ST7735_WriteString(12, 95, "GAME!", Font_11x18, ST7735_BLACK, ST7735_RED);
        }
        else if (c == '5'){
            ST7735_FillScreen(ST7735_GREEN);
            break;
        }
     }
    //  ST7735_WriteString(5, 20, "LAUNCH", Font_7x10, ST7735_BLACK, ST7735_RED);
    //  ST7735_WriteString(15, 60, "PAD", Font_7x10, ST7735_BLACK, ST7735_YELLOW);
    //  ST7735_WriteString(25, 100, "MUSIC", Font_7x10, ST7735_BLACK, ST7735_GREEN);
    //  ST7735_WriteString(35, 140, "GAME!", Font_7x10, ST7735_BLACK, ST7735_CYAN);
}

// int count_score(char state, int score){
//     ST7735_FillScreen(ST7735_GREEN);
//     if (time <= 250){
//         ST7735_WriteString(5, 20, "GOOD", Font_7x10, ST7735_BLACK, ST7735_GREEN);
//         ST7735_WriteString(25, 60, "+1", Font_7x10, ST7735_BLACK, ST7735_GREEN);
//         score += 2;
//     }
//     else if (time <= 500){
//         ST7735_WriteString(5, 20, "WRONG!", Font_7x10, ST7735_BLACK, ST7735_GREEN);
//         ST7735_WriteString(25, 60, "+0", Font_7x10, ST7735_BLACK, ST7735_GREEN);
//         score += 1;
//     }
//     else{
//         ST7735_WriteString(5, 20, "Oops!", Font_7x10, ST7735_BLACK, ST7735_GREEN);
//         ST7735_WriteString(25, 60, "+0", Font_7x10, ST7735_BLACK, ST7735_GREEN);
//     }
//     return score;
// }

// void score_summary(int score){
//     ST7735_FillScreen(ST7735_GREEN);
//     char str_score[20];
//      printf(str_score, "%d", score);
//      ST7735_WriteString(15, 20, "Total:", Font_7x10, ST7735_BLACK, ST7735_GREEN);
//      ST7735_WriteString(30, 60, str_score, Font_7x10, ST7735_BLACK, ST7735_GREEN);
// }

// def()

int main() {
    stdio_init_all();
    ST7735_Init();
    ST7735_DrawImage(0, 0, 80, 160, arducam_logo);
    sleep_ms(1000);
    ST7735_FillScreen(ST7735_GREEN);
     
    gpio_init(PIN_TX);
    gpio_set_function(PIN_TX, GPIO_FUNC_UART);
    uint offset1 = pio_add_program(pio0, &uart_tx_program);
    uart_tx_program_init(pio0, 0, offset1, PIN_TX, SERIAL_BAUD);
    uint offset2 = pio_add_program(pio1, &uart_rx_program);
    uart_rx_program_init(pio1, 0, offset2, PIN_RX, SERIAL_BAUD);
    char c;
    while (true) {
        // uart_tx_program_puts(pio0, 0, "hello");
        // sleep_ms(1000);
        // char c[5];
        // for(int i = 0; i < 5; i++){
        //     c[i] = uart_rx_program_getc(pio1, 0);
        // }
        //printf("test\n");
        //c = uart_rx_program_getc(pio1,0);
        // printf("%s",c);
        // printf("\n");
        // // }
        // printf("test\n");
        c = uart_rx_program_getc(pio1,0);
        
        //ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
        //ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
        //ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
        //ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
        
        switch(c){
            case 's':
                game_init();
                break;
            
            case 'S':
                ST7735_WriteString(18, 30, "Drum", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                ST7735_WriteString(18, 60, "Mode", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                sleep_ms(1000);
                ST7735_FillScreen(ST7735_GREEN);
                char drum_1[9] = "oooooooo";
                char drum_2[9] = "oooooooo";
                char drum_3[9] = "oooooooo";
                char drum_4[9] = "oooooooo";
                
                // for (int j = 1; j < 5; j++){
                // ST7735_WriteString(3,20*j,drum_1,Font_7x10,ST7735_BLACK, ST7735_GREEN);
                //     }
                ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                while (true){
                   
                    char drum = uart_rx_program_getc(pio1,0);
                    
                    if (drum == 'E'){
                        for (int i = 0; i < 8; i++){
                            drum_1[i] = 'o';
                            drum_2[i] = 'o';
                            drum_3[i] = 'o';
                            drum_4[i] = 'o';
                        }
                        
                        
                       ST7735_FillScreen(ST7735_GREEN); 
                       ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                       ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                       ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                       ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                    }

                    else if (drum == 'A'){
                        char num = uart_rx_program_getc(pio1,0);
                        int i = (int)(num) - 48;
                        drum_1[i] = ' ';
                        ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        drum_1[i] = 'x';
                        ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        
                    }
                    else if (drum == 'B'){
                        char num = uart_rx_program_getc(pio1,0);
                        int i = (int)(num) - 48;
                        drum_2[i] = ' ';
                        ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        drum_2[i] = 'x';
                        ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        
                    }
                    else if (drum == 'C'){
                        char num = uart_rx_program_getc(pio1,0);
                        int i = (int)(num) - 48;
                        drum_3[i] = ' ';
                        ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        drum_3[i] = 'x';
                        ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                    
                    }
                    else if (drum == 'D'){
                        char num = uart_rx_program_getc(pio1,0);
                        int i = (int)(num) - 48;
                        drum_4[i] = ' ';
                        ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        drum_4[i] = 'x';
                        ST7735_WriteString(3, 20, drum_1, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 40, drum_2, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 60, drum_3, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(3, 80, drum_4, Font_7x10, ST7735_BLACK, ST7735_GREEN);
                        
                    }
                    else if (drum == 'F'){
                        ST7735_FillScreen(ST7735_GREEN);
                        ST7735_WriteString(18, 30, "Mode", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                        ST7735_WriteString(18, 60, "Stopped", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                        break;
                    }
                    

                    
                }
            case 'L':
                ST7735_WriteString(12, 30, "Music", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                ST7735_WriteString(18, 60, "Mode", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                sleep_ms(500);
                ST7735_WriteString(7, 90, "Enjoy!", Font_11x18, ST7735_RED, ST7735_GREEN);
                char end = uart_rx_program_getc(pio1,0);
                if (end == 'E'){
                    ST7735_FillScreen(ST7735_GREEN);
                    ST7735_WriteString(7, 20, "Thanks", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                    ST7735_WriteString(23, 50, "For", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                    ST7735_WriteString(2, 80, "Playing", Font_11x18, ST7735_BLACK, ST7735_GREEN);
                    break;
                }
            
        }
    }
    
    return 0;
}

