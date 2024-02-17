import {
  AfterViewInit,
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  ElementRef, NgZone,
  ViewChild
} from '@angular/core';
import {JsonPipe, NgIf} from "@angular/common";
import {MenuComponent} from "../menu/menu.component";
//import QrScanner from 'path/to/qr-scanner.min.js'; // if using plain es6 import
import QrScanner from 'qr-scanner';
import {MatButtonModule} from "@angular/material/button";
import {MatInputModule} from "@angular/material/input";
import {MatFormFieldModule} from "@angular/material/form-field";
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import {Subject} from 'rxjs';
import {UserService} from "../services/user.service";


@Component({
  selector: 'app-scan',
  standalone: true,
  imports: [
    MenuComponent, MatButtonModule, NgIf,
    MatInputModule, MatFormFieldModule, FormsModule,
    ReactiveFormsModule, JsonPipe],
  templateUrl: './binding.component.html',
  styleUrl: './binding.component.css',
  changeDetection: ChangeDetectionStrategy.Default
})
export class BindingComponent implements AfterViewInit {
  @ViewChild('video') videoElem!: ElementRef;
  result: string = "";
  scanner: any;
  scanOn: boolean = false;
  hasScannedResult = false;
  scanIsPlace = true;
  bindingMode = false;
  resultChanges = new Subject<string>();
  cameraId = 0;
  camList: any = [];
  cameraInitialized = false;
  resultChanges$ = this.resultChanges.asObservable();
  nameFormControl = new FormControl('', [Validators.required]);

  constructor(private cd: ChangeDetectorRef, private ngZone: NgZone, private userService: UserService) {
  }

  ngOnInit() {
    //QrScanner.WORKER_PATH = './assets/js/qr-scanner-worker.min.js';
    //console.log(this.videoElem);
    //const qrScanner = new QrScanner(this.videoElem.nativeElement, result => {
    //  this.result = result;
    //});
    //qrScanner.start();
    this.resultChanges$.subscribe((result) => {
      //
      this.ngZone.run(() => {
        this.processResult(result);
      })
    })
  }

  ngAfterViewInit() {
    //console.log('hm',this.videoElem);

    //this.scanner.start();
  }

  processResult(result: string) {
    if (result.trim() && this.result != result) {

      console.log('отсканировано2 ', result);
      if (result.indexOf('place:') > -1) {
        // отсканировали место
        console.log('отсканировано место')
        this.result = result;
        this.hasScannedResult = true;
        this.scanIsPlace = true;


        //делаем запрос на бэк, чтобы получить инпормацию от этом месте, есть ли она в бд
        // this.userService.getPlaceInfo(result);

        // если нет, то тогда делаем новую привязку
        this.bindingMode = true;

        this.stopScan();
      } else if (result.indexOf('item:') > -1) {
        // отсканировали предмет
        this.stopScan();
        this.result = result;
        this.hasScannedResult = true;
        this.scanIsPlace = false;

        //делаем запрос на бэк, чтобы получить инпормацию от этом предмете, есть ли она в бд
        // this.userService.getProductInfo(result);

        // если нет, то тогда делаем новую привязку
        this.bindingMode = true;

        this.stopScan();

      } else {
        // отсканировали что-то еще и игнорим это
      }
    }
  }

  startScan() {
    setTimeout(() => {
      if (!this.cameraInitialized) {
        QrScanner.WORKER_PATH = './assets/js/qr-scanner-worker.min.js';
        //console.log(this.videoElem);
        this.scanner = new QrScanner(this.videoElem.nativeElement, result => {
          console.log('отсканировано ', result, typeof result);
          this.resultChanges.next(result?.data?.toString());
        }, {
          highlightScanRegion: true,
          highlightCodeOutline: true,
        });
        this.cameraInitialized = true;
      }

      this.scanner.start().then(() => {
        // получаем список доступных камер
        QrScanner.listCameras(true).then(
          cameras => {
            this.camList = cameras;
          }
        )
      });
      this.scanOn = true;
      this.result = "";
      console.log('after start')
    }, 0);
  }

  stopScan() {
    this.scanner.stop();
    console.log('сканнер остановлен')
    this.scanOn = false;
    console.log('this',this);
    //this.cd.detectChanges();
    this.cd.markForCheck();
    //setTimeout(() => {
    //  this.cd.detectChanges();
    //}, 0)
  }

  switchCamera() {
    //console.log('current', this.camList[this.cameraId], this.camList.length);
    this.cameraId++;
    this.cameraId = this.cameraId % this.camList.length;
    //console.log('next ', this.camList[this.cameraId], this.cameraId);
    this.scanner.setCamera(this.camList[this.cameraId].id);
  }

  toggleFlash() {
    this.scanner.toggleFlash();
    //this.cd.markForCheck();
    //this.cd.detectChanges();
  }
}
