import System.IO

increased (x:v:xs) = (x < v) : increased (v:xs)
increased _ = [False]

increased3 (a:b:c:d:xs) = ((a+b+c) < (b+c+d)) : increased3 (b:c:d:xs)
increased3 _ = [False]

trues x = length (filter (==True) x)

main :: IO ()
main = do
 inputs <- readFile "input.txt"
 let x = map (\x -> read x::Int) (lines inputs)
 print (trues (increased x)) -- part 1
 print (trues (increased3 x)) -- part 2
