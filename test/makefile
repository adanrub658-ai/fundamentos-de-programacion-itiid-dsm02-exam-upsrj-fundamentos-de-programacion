# Makefile located inside tests/
# Compiles and runs unit tests for the clock functions
# Generates ../build/bin/test-clock

CC      := gcc
CFLAGS  := -Wall -O2 -DUNIT_TEST

SRC_DIR := ../src
OBJ_DIR := ../build/obj
BIN_DIR := ../build/bin
TEST_BIN_DIR := $(BIN_DIR)/test

# Default rule: run all unit tests
all: unit-test

# Rule to build and run the clock unit tests
unit-test: test_main.c $(SRC_DIR)/main.c $(SRC_DIR)/clock_stubs.c
	@mkdir -p $(TEST_BIN_DIR)
	$(CC) $(CFLAGS) $^ -o $(TEST_BIN_DIR)/test_main
	@echo "Running clock unit tests..."
	@$(TEST_BIN_DIR)/test_main

clean:
	@rm -rf $(TEST_BIN_DIR)
	@echo "Test binaries removed"