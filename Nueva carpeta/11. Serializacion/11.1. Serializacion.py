import pickle 

ln = ["Pedro","Juan","Manuel"]
bin_ = open("bin.txt","wb")   # Write binario
pickle.dump(ln,bin_)
bin_.close

bin_ = open("bin.txt","rb+")   # Read binario tambien write
rln = pickle.load(bin_)
print(rln)
bin_.close()

del bin_