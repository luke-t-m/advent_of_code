import System.IO
import Data.Char


nums x = read (filter isDigit x)

lets x = filter isAlpha x

eval [] d h = d*h
eval (x:xs) d h | lets x == "forward" = eval xs d (h + nums x)
                | lets x == "down" = eval xs (d + nums x) h
                | lets x == "up" = eval xs (d - nums x) h

eval2 [] d h a = d*h
eval2 (x:xs) d h a | lets x == "forward" = eval2 xs (d + (nums x)*a) (h + nums x) a
                  | lets x == "down" = eval2 xs d h (a + nums x)
                  | lets x == "up" = eval2 xs d h (a - nums x)


main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 print (eval x 0 0)      --part1
 print (eval2 x 0 0 0)   --part2
























