
f1 <- function(x){
    X <- c(0,1,2,3,4,5,6,7,8,9,10)
    if  (!(x %in% X)){
        stop("La fonction f1 est définie sur l'ensemble des entiers compris entre 0 et 10.")}
    else{
        if (x %in% c(0,1,2,3)){
            0.25}
        else{
            0.}}
}

f2 <- function(x){
    X <- c(0,1,2,3,4,5,6,7,8,9,10)
    if (!(x %in% X)){
        stop("La fonction f2 est définie sur l'ensemble des entiers compris entre 0 et 10.")}
    else{
        if (x %in% c(0,1,2,3)){
            0.15}
        else{
            0.}}
}

f3 <- function(x){
    X <- c(0,1,2,3,4,5,6,7,8,9,10)
    if (!(x %in% X)){
        stop("La fonction f3 est définie sur l'ensemble des entiers compris entre 0 et 10.")}
    else{
        if (x %in% c(0,5)){
            0.03}
        else if (x %in% c(1,4)){
            0.16}
        else if (x %in% c(2,3)){
            0.31}
        else{
            0.}}
}

f4 <- function(x){
    X <- c(0,1,2,3,4,5,6,7,8,9,10)
    if (!(x %in% X)){
        stop("La fonction f4 est définie sur l'ensemble des entiers compris entre 0 et 10.")}
    else{
        if (x == 0){
            0.3}
        else if (x == 1){
            0.21}
        else if (x == 2){
            0.15}
        else if (x == 3){
            0.1}
        else if (x == 4){
            0.07}
        else if (x == 5){
            0.05}
        else if (x == 6){
            0.04}
        else if (x == 7){
            0.02}
        else if (x == 8){
            0.02}
        else if (x == 9){
            -0.01}
        else if (x == 10){
            0.03}}
}