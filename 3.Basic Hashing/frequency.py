class Soultion:

    def frequency_OPT(arr, n):
        mp = {}
        for i in range(n):
            if arr[i] in mp:
                mp[arr[i]] += 1
            else:
                mp[arr[i]] = 1
        for x in mp:
            print(x, mp[x])

        print(mp)

        # for i in range(97, 123):
            # print(chr(i))
            # ord(i)


arr = [10, 5, 10, 15, 10, 5]
# arr = 'test'
n = len(arr)
Soultion.frequency_OPT(arr, n)
