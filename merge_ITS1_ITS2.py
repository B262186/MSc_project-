from Bio import SeqIO

its1_records = SeqIO.to_dict(SeqIO.parse("ITS1.fasta", "fasta"))
its2_records = SeqIO.to_dict(SeqIO.parse("ITS2.fasta", "fasta"))

with open("ITS1_ITS2_combined.fasta", "w") as out:
    for key in its1_records:
        if key in its2_records:
            combined_seq = its1_records[key].seq + its2_records[key].seq
            out.write(f">{key}\n{combined_seq}\n")
        else:
            print(f"Warning: {key} not found in ITS2")
