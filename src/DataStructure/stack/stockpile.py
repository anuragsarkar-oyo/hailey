
def stockpile(price, S): 
      
    n = len(price) 
    st = []  
    st.append(0)     # Span value of first element is always 1 
    S[0] = 1
    for i in range(1, n): 
        while( len(st) > 0 and price[st[-1]] <= price[i]): 
            st.pop() 
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1]) 
        st.append(i) 
      
  
arr = [100, 80, 60, 70, 60, 75, 85]
S = [0 for i in range(len(arr)+1)] 
stockpile(arr, S)

    