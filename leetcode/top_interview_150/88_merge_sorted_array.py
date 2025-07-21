def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    WORKSPACE
    ----------
        nums1 has m+n elements [2,0]
        nums2 has n elements [1]
    """
    for index in range(m + n):
        nums2_completed = True if not nums2 else False

        if nums2_completed:
            break
        # Compare the current element from nums1 with first element in nums2
        if not nums2_completed:
            if nums1[index] >= nums2[0]:
                nums1.insert(index, nums2.pop(0))

    for count in range(n):
        nums1.pop()
    nums1.extend(nums2)
    print(f"nums1: {nums1}")
    print(f"nums2: {nums2}")

merge(nums1=[-20,-10,0,0,0], m=2, nums2=[4,5,6], n=3)
merge(nums1=[1], m=1, nums2=[], n=0)
merge(nums1=[0], m=0, nums2=[1], n=1)
print("*"*20)
l1 = [1,2,3,0,0,0]
l2 = [2,5,6]
merge(nums1=l1, m=3, nums2=l2, n=3)
print(f"l1: {l1}")
print(f"l2: {l2}")
