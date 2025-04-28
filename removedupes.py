import os

# Due to github some files got duplicated, used to remove them
data_dir = "/Users/bramdewaal/Desktop/Uni/VSC/Deep Learning/Assignment/Train"

for root, _, files in os.walk(data_dir):
    for fname in files:
        # look only at the “ copy” names
        if fname.endswith(" 2.wav"):
            orig = fname.replace(" 2.wav", ".wav")
            dup_path  = os.path.join(root, fname)
            orig_path = os.path.join(root, orig)
            # only delete if the original exists
            if os.path.exists(orig_path):
                os.remove(dup_path)
                print(f"Removed duplicate file: {dup_path}")
