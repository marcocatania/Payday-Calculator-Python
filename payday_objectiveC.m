//
//  ViewController.m
//  Payday
//
//  Created by Marco Catania on 15/01/2018.
//  Copyright © 2018 Marco Catania. All rights reserved.
//

#import "ViewController.h"

float computePersonalAllowanceDecrease(float payGrossMonth){
    float decreaseAllowance;
    
    decreaseAllowance = (payGrossMonth - 8333.33) / 2;
    return decreaseAllowance;
}

float computePayGrossMonth(float contractualHours, float extraHours, float rate, int weeks){
    float payGrossMonth;
    
    payGrossMonth = ((contractualHours * weeks) + extraHours) * rate;
    return fabsf(payGrossMonth);
}

float computeNInsuranceMonth(float payGrossMonth){
    float nInsuranceMonth;
    
    if(payGrossMonth > 680.00 && payGrossMonth <= 3750.00){
        nInsuranceMonth = ((payGrossMonth - 680.00) * 12) / 100;}
    else if(payGrossMonth > 3750.00){
        nInsuranceMonth = (((3750.00 - 680.00) * 12) / 100) + (((payGrossMonth - 3750.00) * 2) / 100);}
    else{
        nInsuranceMonth = 0.00;
    }
    return fabsf(nInsuranceMonth);
}

float computeIncomeTaxMonth(float payGrossMonth){
    float incomeTaxMonth;
    
    if(payGrossMonth > 959.08 && payGrossMonth <= 3750.00){
        incomeTaxMonth = ((payGrossMonth - 959.08) * 20) / 100;}
    else if(payGrossMonth > 3750.00 && payGrossMonth <= 8333.33) {
        incomeTaxMonth = (((3750.00 - 959.08) * 20) / 100) + (((payGrossMonth - 3750.00) * 40) / 100);}
    else if(payGrossMonth > 8333.33 && payGrossMonth <= 12500.00){
        incomeTaxMonth = ((((3750.00 - (959.08 - ((payGrossMonth - 8333.33) / 2))) * 20)) / 100) + (((payGrossMonth - 3750.00) * 40) / 100);
    }
    else if (payGrossMonth > 12500.00) {
        incomeTaxMonth = ((3750.00 * 20) / 100) + (((payGrossMonth - 3750.00) * 40) / 100) +(((payGrossMonth - 12500.00) * 45) / 100);}
    else{
        incomeTaxMonth = 0;
    }
    return fabsf(incomeTaxMonth);
}

float computeNetPayMonth(float payGrossMonth, float nInsuranceMonth, float incomeTaxMonth){
    float netPayMonth;
    
    netPayMonth = (payGrossMonth) - (nInsuranceMonth + incomeTaxMonth);
    return fabsf(netPayMonth);
}

@interface ViewController ()


@property (weak, nonatomic) IBOutlet UITextField *contractualHoursField;

@property (weak, nonatomic) IBOutlet UITextField *extraHoursField;

@property (weak, nonatomic) IBOutlet UITextField *rateField;

@property (weak, nonatomic) IBOutlet UITextField *weeksField;

@property (weak, nonatomic) IBOutlet UISegmentedControl *segmentedController;

@property (weak, nonatomic) IBOutlet UILabel *resultLabel;


@end

@implementation ViewController
- (IBAction)computeButton:(id)sender {
    NSMutableString *buf = [NSMutableString new];
    
    float contractualHours = [self.contractualHoursField.text floatValue];
    float extraHours = [self.extraHoursField.text floatValue];
    float rate = [self.rateField.text floatValue];
    int weeks = [self.weeksField.text intValue];
    
    float payGrossMonth = computePayGrossMonth(contractualHours, extraHours, rate, weeks);
    float nInsuranceMonth = computeNInsuranceMonth(payGrossMonth);
    float incomeTaxMonth = computeIncomeTaxMonth(payGrossMonth);
    float netPayMonth = computeNetPayMonth(payGrossMonth, nInsuranceMonth, incomeTaxMonth);
    
    if(self.segmentedController.selectedSegmentIndex == 0){
        [buf appendString: [@(payGrossMonth) stringValue]];
    }
    else if(self.segmentedController.selectedSegmentIndex == 1){
        [buf appendString: [@(nInsuranceMonth) stringValue]];
    }
    else if(self.segmentedController.selectedSegmentIndex == 2){
        [buf appendString: [@(incomeTaxMonth) stringValue]];
    }
    else{
        [buf appendString: [@(netPayMonth) stringValue]];
    }
    
    
    self.resultLabel.text = buf;
}

- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
    
    [[self view] endEditing:TRUE];
    
}

- (void)viewDidLoad {
    [super viewDidLoad];
    
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}



@end
