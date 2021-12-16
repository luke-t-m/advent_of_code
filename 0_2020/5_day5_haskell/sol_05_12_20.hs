import System.IO
import Data.List

rowNo [] u l = round (l-1)
rowNo (x:xs) l u | x `elem` "FL" = rowNo xs l (l+(u-l)/2) 
                 | x `elem` "BR" = rowNo xs (l+(u-l)/2) u

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map (splitAt 7) (lines input)
 let ids = [8*(rowNo y 0 128) + (rowNo z 0 8) | (y,z) <- x]
 print (maximum ids)                              --part 1
 print [ a | a <- [99..974], not (a `elem` ids)]  --part 2
