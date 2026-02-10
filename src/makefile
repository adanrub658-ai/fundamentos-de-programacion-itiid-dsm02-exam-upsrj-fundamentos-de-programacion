# Makefile located inside src/
# Compiles main.c into object files and final binary
# Generates ../build/bin, ../build/obj, and ../build/log

CC      := gcc
CFLAGS  := -Wall -O2 -Wno-unused-result
SRC     := main.c
OBJ_DIR := ../build/obj
BIN_DIR := ../build/bin
LOG_DIR := ../build/log

FILENAME := main
TARGET   := $(BIN_DIR)/$(FILENAME)
OBJS     := $(OBJ_DIR)/$(FILENAME).o
LOGS     := $(LOG_DIR)/$(FILENAME).log

# Default rule: build the executable
all: $(TARGET)

# Link object files into final binary
$(TARGET): $(OBJS)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $^ -o $@
	@echo "Executable generated at $(TARGET)"

# Compile source into object files
$(OBJ_DIR)/%.o: %.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@
	@echo "Object file generated at $@"

# Run the program
run: $(TARGET)
	@$(TARGET)

# Run the program and save output to a .log file in build/log
run-save: $(TARGET)
	@mkdir -p $(LOG_DIR)
	@$(TARGET) | tee $(LOGS)
	@echo "Output saved to $(LOGS)"

# Clean up build directories
clean:
	@rm -rf ../build
	@echo "Build directory removed"