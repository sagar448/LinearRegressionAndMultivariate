import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class LinearRegression {
	public static double m = 7.0;
	public static int numberOfRuns = 1000;
	public static void main(String[] args) {
		List<Integer> x = new ArrayList<Integer>(Arrays.asList(150, 200, 250, 300, 350, 400, 600));
		List<Integer> y = new ArrayList<Integer>(Arrays.asList(6450, 7450, 8450, 9450, 11450, 15450, 18450));
		double alpha = 0.0000007;
		int valueToPredict = 700;
		List<Double> bestThetas = runner(x, y, alpha);
		System.out.printf("Values of Thetas are %6f and %6f\n", bestThetas.get(0), bestThetas.get(1));
		System.out.printf("House of square feet %4d is roughly %4f", valueToPredict, hTheta(bestThetas.get(0), bestThetas.get(1), valueToPredict));
	}
	
	static double hTheta(double theta0, double theta1, int x){
		return theta0 + (theta1*x);
	}
	
	static List<Double> GradientDescent(double theta0, double theta1, List<Integer> x, List<Integer> y, double alpha){
		double sum1 = 0.0;
		double sum2 = 0.0;
		for (int i = 0; i<x.size(); i++){
			sum1 = sum1 + ((hTheta(theta0, theta1, x.get(i))) - y.get(i));
			sum2 = sum2 + (((hTheta(theta0, theta1, x.get(i))) - y.get(i))*x.get(i));
		}
		double temp0 = theta0 - (alpha*(1.0/m)*sum1);
		double temp1 = theta1 - (alpha*(1.0/m)*sum2);
		theta0 = temp0;
		theta1 = temp1;
		List<Double> thetas = new ArrayList<Double>(Arrays.asList(theta0, theta1));
		return thetas;
	}
	
	static double costFunction(double theta0, double theta1, List<Integer> x, List<Integer> y){
		double sum1 = 0.0;
		for (int i = 0; i<x.size(); i++){
			sum1 = sum1 + Math.pow(((hTheta(theta0, theta1, x.get(i))) - y.get(i)), 2.0);
		}
		return ((1.0/(2.0 * m))*sum1);
	}
	
	static List<Double> runner(List<Integer> x, List<Integer> y, double alpha){
		double theta0 = 0.0;
		double theta1 = 0.0;
		double bestTheta0 = 0.0;
		double bestTheta1 = 0.0;
		double currCost = costFunction(theta0, theta1, x, y);
		for (int i = 0; i<numberOfRuns; i++){
			List<Double> thetas = GradientDescent(theta0, theta1, x, y, alpha);
			double newCost = costFunction(thetas.get(0), thetas.get(1), x, y);
			if (newCost < currCost){
				currCost = newCost;
				bestTheta0 = thetas.get(0);
				bestTheta1 = thetas.get(1);
			}
		}
		List<Double> bestThetas = new ArrayList<Double>(Arrays.asList(bestTheta0, bestTheta1));
		return bestThetas;
	}
	
	
}
