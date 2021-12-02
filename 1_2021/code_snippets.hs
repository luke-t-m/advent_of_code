import System.IO
import Data.Char
import Data.List
import Data.List.Unique


--shamelessly stolen from Philip Wadler's intro to FP slides on combinatorics
choose :: Int -> [a] -> [[a]]
choose 0 [] = [[]]
choose k (x:xs)
 | k == 0 = [[]]
 | k == n = [x:xs]
 | 0 < k && k < n = choose k xs ++
   map (x:) (choose (k-1) xs)
  where n = length (x:xs)

elemAllC l x = and [ m `elem` x | m <- l ]

splitAny l x = filter (\y -> y /= "" && y /= "\n") (splitAnyW l [x])

splitAnyW [] x = x
splitAnyW (l:ls) x = splitAnyW ls (concat (map (split (onSublist l)) x))

nums x = read (filter isDigit x)
lets x = filter isAlpha x







main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 print (x)
