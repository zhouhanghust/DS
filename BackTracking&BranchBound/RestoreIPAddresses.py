# -- coding:utf-8 --

# Restore IP Addresses(Medium)

# Given "25525511135",
# return ["255.255.11.135", "255.255.111.35"].


def restoreIpAddresses(s):
    addresses = []
    tempAddress = ''
    doRestore(0,tempAddress,addresses,s)
    return addresses


def doRestore(k, tempAddress, addresses, s):
    if k == 4 or len(s) == 0:
        if k==4 and len(s)==0:
            addresses.append(tempAddress)
        return

    i = 0
    while i < len(s) and i <= 2:

        if i != 0 and s[0] == '0':
            break

        part = s[:i+1]
        if int(part) <= 255:
            if len(tempAddress) != 0:
                part = "." + part

            tempAddress += part
            doRestore(k+1,tempAddress,addresses,s[i+1:])
            tempAddress = tempAddress[:len(tempAddress)-len(part)]

        i += 1


if __name__ == "__main__":
    s = "25525511135"
    print(restoreIpAddresses(s))





