import System.IO
import Data.List
import Data.List.Split
import Data.Char

splitAny l x = filter (\y -> y /= "" && y /= "\n") (splitAnyW l [x])

splitAnyW [] x = x
splitAnyW (l:ls) x = splitAnyW ls (concat (map (splitOn l) x))


sens x = joiner ("0" : splitAny ["bags","bag","contain",","," ","."] x)


joiner (n:a:b:xs) = n : (a ++ " " ++ b) : joiner xs
joiner ("no":["other"]) = ["no other"]
joiner [] = []

gold = ["0","shiny gold","1","dark olive","2","vibrant plum"]

inBag x [] = 0
inBag x (n:b:bs) | "no other" `elem` b = 1
                 | read (head n) == 0 = inBag x bs
                 | otherwise = (read (head n)) * (goBag x b) + (inBag x bs)
inBag _ _ = 0
goBag x b = inBag x (head (filter (\y -> y!!1==b) x))



trues x = length (filter (==True) x)

main :: IO()
main = do
 input <- readFile "example.txt"
 let x = map sens (lines input)
 print (inBag [x] [gold])

