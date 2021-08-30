let maxCount = function(m,n,ops){
    let minWidth = m
    let minHeight = n
    for(x of ops){
        minWidth = Math.min(x[0],minWidth)
        minHight = Math.min(x[1],minHeight)
    }
    return minWidth + minHeight
}