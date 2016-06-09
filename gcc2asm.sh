#!/bin/bash

fullname=$1
filename=$(basename $1)
extension="${filename##*.}"
filename="${filename%.*}"
DISABLE1="-fno-asynchronous-unwind-tables \
         -fno-dwarf2-cfi-asm"
DISABLE="-fno-asynchronous-unwind-tables \
         -fno-dwarf2-cfi-asm \
         -fno-builtin \
         -fno-ira-share-save-slots \
         -fno-ira-share-spill-slots \
         -fno-branch-count-reg \
         -fno-default-inline \
         -fno-defer-pop \
         -fno-function-cse \
         -fno-guess-branch-probability \
         -fno-inline \
         -fno-math-errno \
         -fno-peephole \
         -fno-peephole2 \
         -fno-sched-interblock \
         -fno-sched-spec \
         -fno-signed-zeros \
         -fno-toplevel-reorder \
         -fno-trapping-math \
         -fno-zero-initialized-in-bss \
         -fno-common \
         -fno-ident \
         -fno-jump-tables \
         -fno-stack-limit"

gcc -Os -S -masm=intel -m32 $DISABLE1 ${fullname} -o ${filename}.masm

# remove MASM syntax
cat ${filename}.masm | sed -E -e 's/(PTR |OFFSET FLAT:)//' > ${filename}.asm
rm ${filename}.masm
