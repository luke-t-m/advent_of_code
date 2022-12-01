import System.IO
import Data.Char
import Data.List
import Data.List.Unique



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
