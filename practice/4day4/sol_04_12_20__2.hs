import System.IO
import Data.List
import Data.List.Split
import Data.Char


elemAllC l x = and [ m `elem` x | m <- l ]

splitAny l x = filter (\y -> y /= "" && y /= "\n") (splitAnyW l [x])

splitAnyW [] x = x
splitAnyW (l:ls) x = splitAnyW ls (concat (map (split (onSublist l)) x))

nums x = read (filter isDigit x)
digs x = filter isDigit x
lets x = filter isAlpha x
nosp x = filter (/=' ') x

good [] = []
good ("cid:":_:xs) = good xs
good ("byr:":v:xs) = (nums v >= 1920 && nums v <= 2002) : good xs
good ("iyr:":v:xs) = (nums v >= 2010 && nums v <= 2020) : good xs
good ("eyr:":v:xs) = (nums v >= 2020 && nums v <= 2030) : good xs
good ("hcl:":v:xs) = (head v == '#' && elemAllC (lets v) "abcdef0123456789" && length (nosp t) == 6) : good xs where t = tail v
good ("ecl:":v:xs) = ((nosp v) `elem` ["amb","blu","brn","gry","grn","hzl","oth"]) : good xs
good ("pid:":v:xs) = (length (digs v) == 9) : good xs
good ("hgt:":v:xs) | lets v == "in" = (nums v >= 59 && nums v <= 76) : good xs
                   | lets v == "cm" = (nums v >= 150 && nums v <= 193) : good xs
                   | otherwise = False : good xs


main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map (splitAny filtList) (splitOn "\n\n" input)
 print (length (filter (==7) (map (length . filter (==True) . good) x)))
  where filtList = ["\n","ecl:","pid:","eyr:","hcl:","byr:","iyr:","hgt:","cid:"]
