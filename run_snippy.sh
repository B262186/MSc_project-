#!/bin/bash

REF="S288C_reference.fasta"

SAMPLES=(
"CLIB413_ERR1308868"
)

for SAMPLE in "${SAMPLES[@]}"
do
  echo "Running Snippy on $SAMPLE"
  snippy --cpus 16 \
    --ref $REF \
    --R1 ${SAMPLE}_1.fastq \
    --R2 ${SAMPLE}_2.fastq \
    --outdir snippy_${SAMPLE}
done
