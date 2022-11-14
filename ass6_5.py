text = "X-DSPAM-Confidence:    0.8475"
end=len(text)
start=text.find('0')
sdig=text[start:]
idig=float(sdig)
print(idig)
