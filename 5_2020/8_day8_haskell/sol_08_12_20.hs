import System.IO
import Data.Char

nums x = read (filter (\y -> isDigit y || y == '-') x)
lets x = filter isAlpha x

run x v a p | p `elem` v = a
            | lets t == "nop" = run x (p:v) a (p+1)
            | lets t == "acc" = run x (p:v) (a+nums t) (p+1)
            | lets t == "jmp" = run x (p:v) a (p+nums t)
 where t = x!!p


main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 print (run x [] 0 0)
