.PHONY: all clean

OBJS_DIR = objs
SRCS_DIR = src
LIBS_DIR = /usr/local/lib
INCS_DIR = /usr/local/include

DEST_PREFIX_DIR = /tmp

CC=gcc
CFLAGS=-Wall -Werror -fpic -c -L $(LIBS_DIR) -I $(INCS_DIR)
LFLAGS=-shared

RM = rm -rf

LIBS = -lssl -lcrypto
TESTS_LIBS := -lcheck

_OBJS = quicksort.o
OBJS = $(patsubst %,$(OBJS_DIR)/%,src/$(_OBJS))

_TEST_OBJS = check_quicksort.o
TEST_OBJS = $(patsubst %,$(OBJS_DIR)/%,tests/$(_TEST_OBJS))


all: quicksort.so

$(OBJS_DIR):
	-@mkdir -p $(OBJS_DIR)/src $(OBJS_DIR)/tests

$(OBJS_DIR)/%.o: %.c $(OBJS_DIR)
	$(CC) -c -o $@ $< $(CFLAGS)

clean:
	-$(RM) $(OBJS_DIR) *~ core quicksort.so test
	-@echo ' '

libGeolocation.so: $(OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: GCC C Linker'
	gcc -o $@ $^ $(LFLAGS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '

test: clean $(TEST_OBJS) $(OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: GCC C Linker'
	gcc -o $@ $(TEST_OBJS) $(OBJS) $(TESTS_LIBS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo 'Running tests'
	./$@
	@echo ' '

util: $(UTILS_OBJS) $(OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: GCC C Linker'
	gcc -o $@ $^ $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '

install: libGeolocation.so
	@mkdir -p $(DEST_PREFIX_DIR)/include $(DEST_PREFIX_DIR)/lib
	@cp $< $(DEST_PREFIX_DIR)/lib
	@echo installed $@ at $(DEST_PREFIX_DIR)/lib
	@cp $(SRCS_DIR)/quicksort.h $(DEST_PREFIX_DIR)/include
	@echo installed quicksort.h at $(DEST_PREFIX_DIR)/include

