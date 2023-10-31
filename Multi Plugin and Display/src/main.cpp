/**
 * @file main.cpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2023-08-26
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <Arduino.h>

#include "version.h"
#include "pins.h"

#include "rapidPlugin_stream.h"
rapidPlugin_stream usbuart("usb");

#include "rapidPlugin_memory.h"
rapidPlugin_memory memory("memory");

#include "rapidPlugin_template.h"
rapidPlugin_template plug1("plug1");
rapidPlugin_template plug2("plug2");

#include "rapidPlugin_display.h"
rapidPlugin_display display("display");

void setup() 
{
  // Run the background memory management
  memory.run();

  // Start Serial for communication
  Serial.begin(Memory.baudRate);
  // while (!Serial) { ; }

  // Run the stream manager to manage Serial
  usbuart.run();
  
  // Set debug level and stream
  rapidRTOS.setDebugStream(&usbuart);
  rapidRTOS.setDebugLevel(Memory.debugLevel);

  // Run template plugins (do not do much)
  plug1.run();
  plug2.run();

  // Run the display and render the canvas
  display.run();
}

void loop() 
{
  // After 15 seconds stop both template plugins
  if (millis() > 15000 && millis() <= 20000)
  {
    plug1.stop();
    plug2.stop();
  }

  // After 20 seconds restart 1 of the plugins
  if (millis() > 20000)
  {
    plug1.run();
  }

  // Every loop print information on both plugins and how many tasks are running
  rapidRTOS.printDebug(1, rapidDebug::INFO, "plug1: %s\n", rapidRTOS.cmd("plug1", "random(0,100)"));
  rapidRTOS.printDebug(1, rapidDebug::INFO, "plug2: %s\n", rapidRTOS.cmd("plug2", "random(1000,2000)"));
  rapidRTOS.printDebug(1, "tasks: %d\n", rapidRTOS.getNumTasks());

  // Every loop sleep for 0.5 seconds
  delay(500);
}