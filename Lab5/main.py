from __future__ import annotations 
import argparse 
import sys 
from typing import List 
import num_series
def build_series(kind: str, n: int, seed: int) -> List[float]: 
 if kind == "random": 
  return num_series.random_series(n, low=-50, high=50, seed=seed) 
 if kind == "sine": 
  return num_series.sine_series(n, amplitude=10, frequency=2, noise=1.5, seed=seed) 
 if kind == "trend": 
  return num_series.trend_series(n, start=0, step=1.0, noise=0.5, seed=seed) 
 raise ValueError(f"Неизвестный тип ряда: {kind!r}") 
def print_series(title: str, values: List[float], fmt: str = "{:>10.3f}") -> None: 
 print(f"\n{title} (n={len(values)}):") 
 print(" " + " ".join(fmt.format(v) for v in values)) 
def print_header(kind: str, n: int) -> None: 
 print("=" * 60) 
 print(f"Тип ряда: {kind}, n = {n}") 
 print("-" * 60) 
def print_stats(stats: dict) -> None:  
 print(f"Среднее арифметическое : {stats['mean']:>10.4f}") 
 print(f"Медиана    : {stats['median']:>10.4f}") 
 print(f"Размах (max - min)  : {stats['spread']:>10.4f}") 
 print(f"min / max    : {stats['min']:>10.4f} / {stats['max']:.4f}") 
def print_footer() -> None: 
 print("=" * 60)
def build_parser() -> argparse.ArgumentParser: 
 parser = argparse.ArgumentParser( 
  description="Алгоритмическая обработка числовых рядов", 
  formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
 ) 
 parser.add_argument( 
  "--kind", choices=["random", "sine", "trend"], default="sine", 
  help="тип генерируемого ряда", 
 ) 
 parser.add_argument( 
  "--n", type=int, default=20, 
  help="количество точек в ряде", 
 ) 
 parser.add_argument( 
  "--window", type=int, default=3, 
  help="размер окна для скользящей средней", 
 ) 
 parser.add_argument( 
  "--alpha", type=float, default=0.3, 
  help="коэффициент сглаживания для EMA, 0 < alpha <= 1", 
 ) 
 parser.add_argument( 
  "--seed", type=int, default=42, 
  help="зерно ГПСЧ для воспроизводимости", 
 ) 
 return parser
def main(argv: List[str] | None = None) -> int:  
 args = build_parser().parse_args(argv) 
 try:
  data = build_series(args.kind, args.n, args.seed) 
  stats = num_series.summarize(data) 
  sma = num_series.simple_moving_average(data, args.window) 
  ema = num_series.exponential_moving_average(data, args.alpha) 
  cma = ( 
   num_series.centered_moving_average(data, args.window) 
   if args.window % 2 == 1 else None 
 ) 
 except ValueError as err: 
  print(f"Ошибка: {err}", file=sys.stderr) 
  return 1
 print_header(args.kind, args.n) 
 print_stats(stats) 
 print_series("Исходный ряд", data) 
 print_series(f"SMA (window={args.window})", sma) 
 print_series(f"EMA (alpha={args.alpha})", ema) 
 if cma is not None: 
  print_series(f"Центрированное MA (window={args.window})", cma) 
 print_footer() 
 return 0 
if __name__ == "__main__": 
 raise SystemExit(main()) 