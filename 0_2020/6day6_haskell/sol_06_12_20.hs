import System.IO
import Data.List
import Data.List.Split

doeet y = [ a | a <- (concat y), (length (filter (==a) (concat y))) == length y ]

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = splitOn "\n\n" input
 print (sum (map (length . filter (/='\n') . nub) x)) --part 1
 let y = map (splitOn "\n") x
 print (sum (map (length . nub . doeet . filter (/="")) y))
